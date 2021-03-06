# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Article(models.Model):
#     idarticle = models.BigAutoField(db_column='idArticle', primary_key=True)  # Field name made lowercase.
#     nom = models.CharField(max_length=50, blank=True, null=True)
#     description = models.CharField(max_length=200, blank=True, null=True)
#     prix = models.FloatField(blank=True, null=True)
#     stock = models.IntegerField(blank=True, null=True)
#     nbventes = models.IntegerField(db_column='nbVentes', blank=True, null=True)  # Field name made lowercase.
#     nbvisiteurs = models.IntegerField(db_column='nbVisiteurs', blank=True, null=True)  # Field name made lowercase.
#     datesortie = models.DateField(db_column='dateSortie', blank=True, null=True)  # Field name made lowercase.
#     idopus = models.PositiveBigIntegerField(db_column='idOpus')  # Field name made lowercase.
#     url = models.CharField(max_length=512, blank=True, null=True)
#     url_alt = models.CharField(max_length=512, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'article'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorie(models.Model):
    idcategorie = models.BigAutoField(db_column='idCategorie', primary_key=True)  # Field name made lowercase.
    nomcategorie = models.CharField(db_column='nomCategorie', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorie'


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
    idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='idClient', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commande'


class Commentaire(models.Model):
    textecommentaire = models.CharField(db_column='texteCommentaire', max_length=255)  # Field name made lowercase.
    datecommentaire = models.DateField(db_column='dateCommentaire')  # Field name made lowercase.
    idcommentaire = models.BigAutoField(db_column='idCommentaire', primary_key=True)  # Field name made lowercase.
    idclient = models.PositiveBigIntegerField(db_column='idClient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commentaire'


class Commenter(models.Model):
    idarticle = models.PositiveBigIntegerField(db_column='idArticle', blank=True, null=True)  # Field name made lowercase.
    idclient = models.PositiveBigIntegerField(db_column='idClient', blank=True, null=True)  # Field name made lowercase.
    idcommentaire = models.PositiveBigIntegerField(db_column='idCommentaire', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commenter'


class Developper(models.Model):
    idstudiodev = models.PositiveBigIntegerField(db_column='idStudioDev', primary_key=True)  # Field name made lowercase.
    idarticle = models.PositiveBigIntegerField(db_column='idArticle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'developper'
        unique_together = (('idstudiodev', 'idarticle'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Editer(models.Model):
    idarticle = models.PositiveBigIntegerField(db_column='idArticle', primary_key=True)  # Field name made lowercase.
    idediteur = models.PositiveBigIntegerField(db_column='idEditeur')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'editer'
        unique_together = (('idarticle', 'idediteur'),)


class Editeur(models.Model):
    idediteur = models.BigAutoField(db_column='idEditeur', primary_key=True)  # Field name made lowercase.
    nomediteur = models.CharField(db_column='nomEditeur', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'editeur'


class Opus(models.Model):
    idopus = models.BigAutoField(db_column='idOpus', primary_key=True)  # Field name made lowercase.
    nomopus = models.CharField(db_column='nomOpus', max_length=50)  # Field name made lowercase.
    idarticle = models.PositiveBigIntegerField(db_column='idArticle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'opus'


class Paiement(models.Model):
    idpaiement = models.BigAutoField(db_column='idPaiement', primary_key=True)  # Field name made lowercase.
    nompaiement = models.CharField(db_column='nomPaiement', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paiement'


class Panier(models.Model):
    nomarticle = models.CharField(db_column='nomArticle', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'panier'


class Posseder(models.Model):
    numcommande = models.PositiveBigIntegerField(db_column='numCommande', primary_key=True)  # Field name made lowercase.
    idarticle = models.PositiveBigIntegerField(db_column='idArticle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'posseder'
        unique_together = (('numcommande', 'idarticle'),)


class Ranger(models.Model):
    idarticle = models.PositiveBigIntegerField(db_column='idArticle', primary_key=True)  # Field name made lowercase.
    idcategorie = models.PositiveBigIntegerField(db_column='idCategorie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ranger'
        unique_together = (('idarticle', 'idcategorie'),)


class Studiodev(models.Model):
    idstudiodev = models.BigAutoField(db_column='idStudioDev', primary_key=True)  # Field name made lowercase.
    nomstudiodev = models.CharField(db_column='nomStudioDev', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studiodev'


class Suivre(models.Model):
    idclient = models.PositiveBigIntegerField(db_column='idClient', primary_key=True)  # Field name made lowercase.
    idarticle = models.PositiveBigIntegerField(db_column='idArticle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'suivre'
        unique_together = (('idclient', 'idarticle'),)


class Utiliser(models.Model):
    numcommande = models.PositiveBigIntegerField(db_column='numCommande', primary_key=True)  # Field name made lowercase.
    idpaiement = models.PositiveBigIntegerField(db_column='idPaiement')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utiliser'
        unique_together = (('numcommande', 'idpaiement'),)


class Wishlist(models.Model):
    idarticle = models.PositiveBigIntegerField(db_column='idArticle', blank=True, null=True)  # Field name made lowercase.
    idclient = models.PositiveBigIntegerField(db_column='idClient', blank=True, null=True)  # Field name made lowercase.
    oldprice = models.FloatField(db_column='oldPrice', blank=True, null=True)  # Field name made lowercase.
    oldstock = models.BigIntegerField(db_column='oldStock', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wishlist'
