import datetime
from django.dispatch import Signal
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from adminInterface.json_datetime_serializer import JSONDateTimeSerializer
from adminInterface.models import DjangoSession, BrowsingHistory
from adminInterface.views import get_game_category
from django.contrib.sessions.models import Session

# object_viewed_signal = Signal()
user_is_on_page = Signal()


@receiver(user_is_on_page)
def user_page(sender, request, **kwargs):
    date = datetime.datetime.now()
    jsondate = JSONDateTimeSerializer.dumps(JSONDateTimeSerializer, date)
    session_key = DjangoSession.objects.get(session_key=request.session.session_key)
    print("oui oui ", session_key)
    print('user is on page {} where the product id is {} at date {}'
          .format(request.get_full_path(), request.GET.get('product', ''), date))
    if request.GET.get('product', '') != '':
        category_name = get_game_category(request.GET.get('product', ''))
        b = BrowsingHistory(session_key=session_key, date=date, url=request.get_full_path(), type=category_name)
        b.save()

