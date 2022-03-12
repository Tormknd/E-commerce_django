from .signals import object_viewed_signal


def send_article_signals(article, request, *args, **kwargs):
    id_article = article.idarticle
    object_viewed_signal.send(article.__class__, instance=id_article, request=request)  # envoi d'un signal
