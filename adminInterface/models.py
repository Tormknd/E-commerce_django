from django.db import models
from django.contrib.contenttypes.models import ContentType


# Create your models here.


class Client(models.Model):
    idclient = models.BigAutoField(db_column='idClient', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=25, blank=True, null=True)
    prenom = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    adresse = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class Commande(models.Model):
    numcommande = models.BigAutoField(db_column='numCommande', primary_key=True)  # Field name made lowercase.
    prixcommande = models.FloatField(db_column='prixCommande', blank=True, null=True)  # Field name made lowercase.
    articletotal = models.IntegerField(db_column='articleTotal', blank=True, null=True)  # Field name made lowercase.
    datecommande = models.DateField(db_column='dateCommande', blank=True, null=True)  # Field name made lowercase.
    idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='idClient', blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commande'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ranger(models.Model):
    idarticle = models.PositiveBigIntegerField(db_column='idArticle', primary_key=True)  # Field name made lowercase.
    idcategorie = models.PositiveBigIntegerField(db_column='idCategorie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ranger'
        unique_together = (('idarticle', 'idcategorie'),)


class BrowsingHistory(models.Model):
    nb = models.AutoField(primary_key=True)
    session_key = models.CharField(max_length=65535)
    date = models.DateTimeField()
    url = models.TextField()
    type = models.TextField()

    class Meta:
        managed = False
        db_table = 'browsing_history'


class Categorie(models.Model):
    idcategorie = models.BigAutoField(db_column='idCategorie', primary_key=True)  # Field name made lowercase.
    nomcategorie = models.CharField(db_column='nomCategorie', max_length=25, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorie'
