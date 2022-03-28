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


class Commenter(models.Model):
    idarticle = models.PositiveBigIntegerField(db_column='idArticle', blank=True,
                                               null=True)  # Field name made lowercase.
    idclient = models.PositiveBigIntegerField(db_column='idClient', blank=True, null=True)  # Field name made lowercase.
    idcommentaire = models.PositiveBigIntegerField(db_column='idCommentaire', blank=True,
                                                   null=True)  # Field name made lowercase.
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'commenter'


class Commentaire(models.Model):
    textecommentaire = models.CharField(db_column='texteCommentaire', max_length=255)  # Field name made lowercase.
    datecommentaire = models.DateField(db_column='dateCommentaire')  # Field name made lowercase.
    idcommentaire = models.BigAutoField(db_column='idCommentaire', primary_key=True)  # Field name made lowercase.
    idclient = models.PositiveBigIntegerField(db_column='idClient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commentaire'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


# def test(sender, instance, request, *args, **kwargs):
#     print("models l.26 ", instance)
#
#
# object_viewed_signal.connect(test)
