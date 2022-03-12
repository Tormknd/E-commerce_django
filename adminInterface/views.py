import datetime

from django.shortcuts import render
from djangoProject.models import Article
from .models import Commande


def home(request):
    article = Article.objects.get(idarticle=7)
    sales = totalSales(request)
    orders = totalOrders(request)
    context = {
        "object": article,
        "sales": sales,
        "orders": orders[0],
        "lastWeekOrders": orders[1],
        "percentage": orders[2]
    }

    return render(request, 'admin/admin.html', context)


def totalSales(request):
    commandList = Commande.objects.all()
    print(commandList)
    prix = 0
    for command in commandList:
        prix += command.prixcommande

    return prix


def totalOrders(request):
    allOrders = Commande.objects.all()
    lastWeekOrdersNum = 0
    currentWeekOrdersNum = 0
    lastWeek = previous_week_range(datetime.datetime.now())
    startLastWeek = datetime.date(lastWeek[0].year, lastWeek[0].month, lastWeek[0].day)
    endLastWeek = datetime.date(lastWeek[1].year, lastWeek[1].month, lastWeek[1].day)

    for order in allOrders:
        date2 = datetime.date(order.datecommande.year, order.datecommande.month, order.datecommande.day)
        print("date2", date2)
        if date2 >= endLastWeek:
            currentWeekOrdersNum += 1
        elif (date2 <= endLastWeek) and (date2 >= startLastWeek):
            print("true")
            lastWeekOrdersNum += 1
    print(currentWeekOrdersNum, lastWeekOrdersNum)
    percentage = percent(lastWeekOrdersNum, currentWeekOrdersNum)

    return currentWeekOrdersNum, lastWeekOrdersNum, percentage


def percent(first, second):
    return (second*100/first)-100


def previous_week_range(date):
    start_date = date + datetime.timedelta(-date.weekday(), weeks=-1)
    end_date = date + datetime.timedelta(-date.weekday() - 1)
    return start_date, end_date
