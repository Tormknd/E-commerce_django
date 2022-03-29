from datetime import datetime
from django.utils import timezone
from django.dispatch import Signal
from django.dispatch import receiver
from datetime import timedelta
from adminInterface.models import DjangoSession, BrowsingHistory
from adminInterface.views import get_game_category, get_last_date_item
from django.contrib.sessions.models import Session

# object_viewed_signal = Signal()
user_is_on_page = Signal()


@receiver(user_is_on_page)
def user_page(sender, request, **kwargs):
    date = timezone.now()
    session_key = DjangoSession.objects.get(session_key=request.session.session_key)
    print(session_key.session_key)
    print('user is on page {} where the product id is {} at date {}'
          .format(request.get_full_path(), request.GET.get('product', ''), date))
    category_name = get_game_category(request.GET.get('product', ''))
    if request.GET.get('product', '') != '':
        if BrowsingHistory.objects.filter(session_key=session_key, url=request.get_full_path()).exists():
            g = get_last_date_item(BrowsingHistory.objects.filter(session_key=session_key, url=request.get_full_path()))
            if g.date + timedelta(hours=2) <= date: # Si 2h sont passé depuis la dernière visite de la session sur cette page
                b = BrowsingHistory(session_key=session_key.session_key, date=date, url=request.get_full_path(), type=category_name)
                b.save()
        else:
            b = BrowsingHistory(session_key=session_key.session_key, date=date, url=request.get_full_path(), type=category_name)
            b.save()
