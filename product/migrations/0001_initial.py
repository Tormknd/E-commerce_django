# Generated by Django 4.0.2 on 2022-03-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('idarticle', models.BigAutoField(db_column='idArticle', primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('prix', models.FloatField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('nbventes', models.IntegerField(blank=True, db_column='nbVentes', null=True)),
                ('nbvisiteurs', models.IntegerField(blank=True, db_column='nbVisiteurs', null=True)),
                ('datesortie', models.DateField(blank=True, db_column='dateSortie', null=True)),
                ('idopus', models.PositiveBigIntegerField(db_column='idOpus')),
                ('url', models.CharField(blank=True, max_length=512, null=True)),
                ('url_alt', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'db_table': 'article',
                'managed': False,
            },
        ),
    ]
