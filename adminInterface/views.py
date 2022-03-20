import datetime
from django.shortcuts import render
from .models import Commande, Ranger, Categorie, BrowsingHistory
from product.models import Article
from .models import DjangoSession
from django.contrib.sessions.models import Session
from .json_datetime_serializer import JSONDateTimeSerializer
from djangoProject.createsession import CreateSession
from django.template.defaulttags import register

from django.contrib.contenttypes.models import ContentType


def home(request):
    CreateSession.session(CreateSession, request)
    clients_device = check_client_device(request)
    article = Article.objects.get(idarticle=7)
    sales = total_sales_of_week(request)
    orders = total_orders(request)
    month_sales = monthly_sales()
    all_sessions_number = weekly_visitors_by_sessions(request)
    time_spent = time_spent_on_category()
    keys = list(time_spent.keys())
    context = {
        "object": article,
        "total_sales": sales[4],
        "weekly_sales": sales[0],
        "sales_percent": sales[3],
        "orders": orders[0],
        "lastWeekOrders": orders[1],
        "order_percentage": orders[2],
        "unique_visitors": all_sessions_number[0],
        "visitors_percentage": all_sessions_number[1],
        "month_sales": month_sales,
        "keys_time_spent": keys,
        "RPG": time_spent['RPG'].seconds,
        "ActionRPG": time_spent['Action-RPG'].seconds,
        "Aventures": time_spent['Aventures'].seconds,
        "Jeux_de_Tirs": time_spent['Jeux de Tirs'].seconds,
        "Simulation": time_spent['Simulation'].seconds,
        "Course_automobile": time_spent['Course automobile'].seconds,
        "user_mobile": clients_device[0],
        "user_desktop": clients_device[1],
    }

    return render(request, 'admin/admin.html', context)


def get_client_ip(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip:
        ip2 = ip.split(',')[0]
    else:
        ip2 = request.META.get('REMOTE_ADDR')

    return ip2


def check_client_device(request):
    keywords = ['Mobile', 'Opera Mini', 'Android']
    user_agent = request.META['HTTP_USER_AGENT']

    if any(word in user_agent for word in keywords):
        request.session['use_mobile'] = True
    else:
        request.session['use_desktop'] = True
        if 'use_mobile' not in request.session:
            request.session['use_mobile'] = False

    list_users = {
        "Mobile": 0,
        "Desktop": 0,
    }
    list_sessions = DjangoSession.objects.all()
    for session in list_sessions:
        sess = Session.objects.get(session_key=session.session_key)
        if sess.get_decoded().get('use_mobile'):
            list_users['Mobile'] += 1
        if sess.get_decoded().get('use_desktop'):
            list_users['Desktop'] += 1

    return list_users['Mobile'], list_users['Desktop']


@register.filter('key')
def get_item(dictionary, key):
    return dictionary.get(key)


def monthly_sales():
    months_sales = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        '10': 0,
        '11': 0,
        '12': 0,
    }
    sales = Commande.objects.all()

    for sale in sales:
        for month in months_sales:
            if sale.datecommande.month.__str__() == month:
                months_sales[month] += sale.prixcommande

    return months_sales


def weekly_visitors_by_sessions(request):
    all_session = DjangoSession.objects.all()
    last_week_end_date = previous_week_range(datetime.datetime.now())[1]
    last_week_start_date = previous_week_range(datetime.datetime.now())[0]
    sessions_of_this_week = 0
    last_week_sessions = 0

    for session in all_session:
        sess = Session.objects.get(session_key=session.session_key)
        json_serialized_date = sess.get_decoded().get('creation_date')
        session_creation_date = JSONDateTimeSerializer.loads(JSONDateTimeSerializer, json_serialized_date)
        if session_creation_date > last_week_end_date:
            sessions_of_this_week += 1
        elif (session_creation_date <= last_week_end_date) and (session_creation_date >= last_week_start_date):
            last_week_sessions += 1

    percentage = percent(last_week_sessions, sessions_of_this_week)

    return sessions_of_this_week, percentage


def time_spent_on_category():
    count = 0
    category_object_name = Categorie.objects.values_list('nomcategorie', flat=True)
    browsing_hist = BrowsingHistory.objects.all()
    category_list = {}
    for x in category_object_name:
        category_list[x] = datetime.timedelta(minutes=0)

    while count < len(browsing_hist) - 1:
        date_difference = browsing_hist[count + 1].date - browsing_hist[count].date
        max_date_diff = datetime.timedelta(minutes=5)
        if browsing_hist[count].type.__str__() in category_list:
            key = browsing_hist[count].type.__str__()
            if date_difference > max_date_diff:
                category_list[key] = category_list.get(key, 0) + datetime.timedelta(minutes=5)
            else:
                category_list[key] = category_list.get(key, 0) + date_difference
        count += 1
    return category_list


def total_sales_of_week(request):
    order_list = Commande.objects.all()
    last_week_orders = 0
    current_week_orders = 0
    # I used a method to find the previous weekend and start date
    last_week_start_date = previous_week_range(datetime.datetime.now())[0]
    last_week_end_date = previous_week_range(datetime.datetime.now())[1]
    this_week_sales = 0
    total_sales = 0
    for order in order_list:
        total_sales += order.prixcommande
        date2 = datetime.datetime(order.datecommande.year, order.datecommande.month, order.datecommande.day)
        if date2 > last_week_end_date:
            this_week_sales += order.prixcommande
            current_week_orders += 1
        elif (date2 <= last_week_end_date) and (date2 >= last_week_start_date):
            last_week_orders += 1

    percentage = percent(last_week_orders, current_week_orders)

    return this_week_sales, current_week_orders, last_week_orders, percentage, total_sales


def total_orders(request):
    all_orders = Commande.objects.all()
    last_week_orders_num = 0
    current_week_orders_num = 0
    # I used a method to find the previous weekend and start date
    last_week_start_date = previous_week_range(datetime.datetime.now())[0]
    last_week_end_date = previous_week_range(datetime.datetime.now())[1]

    for order in all_orders:
        date2 = datetime.datetime(order.datecommande.year, order.datecommande.month, order.datecommande.day)
        if date2 > last_week_end_date:
            current_week_orders_num += 1
        elif (date2 <= last_week_end_date) and (date2 >= last_week_start_date):
            last_week_orders_num += 1
    percentage = percent(last_week_orders_num, current_week_orders_num)

    return current_week_orders_num, last_week_orders_num, percentage  # I returned the data from current and last week
    # and the difference between them in percentage


def percent(last_week, second_week):
    result = 0
    if last_week == 0:
        last_week = 1
        result = ((second_week * 100 / last_week) - 100) + 100  # I add 100 so the result is more logical,
        # e.g: from 0 to 4 visitor it will be +400% increase instead of +300%
    else:
        result = (second_week * 100 / last_week) - 100

    return result


def previous_week_range(date):
    # Method to find the last week start and end date
    start_date = date + datetime.timedelta(-date.weekday(), weeks=-1)
    end_date = date + datetime.timedelta(-date.weekday() - 1)
    return start_date, end_date


def get_game_category(game_id):
    game_category_id = Ranger.objects.get(idarticle=game_id).idcategorie
    category_name = Categorie.objects.get(idcategorie=game_category_id).nomcategorie
    return category_name


def get_last_date_item(obj):
    item = 0
    if len(obj) > 1:
        count = 0
        while count < len(obj) - 1:
            if obj[count].date < obj[count + 1].date:
                item = obj[count + 1]
            count += 1
        return item
    else:
        item = obj.first()
        return item
