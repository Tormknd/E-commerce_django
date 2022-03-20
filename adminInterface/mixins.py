# from .signals import object_viewed_signal
from .signals import user_is_on_page


# def send_article_signals(article, request, *args, **kwargs):
#     id_article = article.idarticle
#     object_viewed_signal.send(article.__class__, instance=id_article, request=request)  # envoi d'un signal


def send_on_page_signals(request, *args, **kwargs):
    page = request.META.get('HTTP_REFERER')
    user_is_on_page.send(page, request=request)

