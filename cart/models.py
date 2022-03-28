from django.db import models


# Create your models here.
class Posseder(models.Model):
    numcommande = models.BigIntegerField(db_column='numCommande')  # Field name made lowercase.
    idarticle = models.PositiveBigIntegerField(db_column='idArticle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'posseder'
