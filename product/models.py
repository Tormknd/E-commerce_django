from django.db import models
# from adminInterface.signals import object_viewed_signal

# Create your models here.


class Article(models.Model):
    idarticle = models.BigAutoField(db_column='idArticle', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    prix = models.FloatField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    nbventes = models.IntegerField(db_column='nbVentes', blank=True, null=True)  # Field name made lowercase.
    nbvisiteurs = models.IntegerField(db_column='nbVisiteurs', blank=True, null=True)  # Field name made lowercase.
    datesortie = models.DateField(db_column='dateSortie', blank=True, null=True)  # Field name made lowercase.
    idopus = models.PositiveBigIntegerField(db_column='idOpus')  # Field name made lowercase.
    url = models.CharField(max_length=512, blank=True, null=True)
    url_alt = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


# def test(sender, instance, request, *args, **kwargs):
#     print("models l.26 ", instance)
#
#
# object_viewed_signal.connect(test)

