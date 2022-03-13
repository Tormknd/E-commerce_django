import datetime
import base64

from django.shortcuts import render
from product.models import Article
from .models import Commande
from .models import DjangoSession
from django.contrib.sessions.models import Session
from .json_datetime_serializer import JSONDateTimeSerializer
from djangoProject.createsession import CreateSession
from .signals import object_viewed_signal
from django.contrib.contenttypes.models import ContentType


def home(request):
    CreateSession.session(CreateSession, request)
    article = Article.objects.get(idarticle=7)
    sales = total_sales(request)
    orders = total_orders(request)
    all_sessions_number = weekly_visitors_by_sessions(request)
    context = {
        "object": article,
        "sales": sales[0],
        "sales_percent": sales[3],
        "orders": orders[0],
        "lastWeekOrders": orders[1],
        "order_percentage": orders[2],
        "unique_visitors": all_sessions_number[0],
        "visitors_percentage": all_sessions_number[1]
    }

    return render(request, 'admin/admin.html', context)


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


def total_sales(request):
    order_list = Commande.objects.all()
    last_week_orders = 0
    current_week_orders = 0
    # I used a method to find the previous weekend and start date
    last_week_start_date = previous_week_range(datetime.datetime.now())[0]
    last_week_end_date = previous_week_range(datetime.datetime.now())[1]
    price = 0
    for order in order_list:
        price += order.prixcommande
        date2 = datetime.datetime(order.datecommande.year, order.datecommande.month, order.datecommande.day)
        if date2 > last_week_end_date:
            current_week_orders += 1
        elif (date2 <= last_week_end_date) and (date2 >= last_week_start_date):
            last_week_orders += 1

    percentage = percent(last_week_orders, current_week_orders)
    print(percentage)

    return price, current_week_orders, last_week_orders, percentage


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
