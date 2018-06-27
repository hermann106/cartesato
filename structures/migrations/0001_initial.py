# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 12:05
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Structures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etablis_id', models.CharField(max_length=254)),
                ('nom_fs', models.CharField(max_length=254)),
                ('localite', models.CharField(max_length=254)),
                ('region', models.CharField(max_length=254)),
                ('district', models.CharField(max_length=254)),
                ('type', models.CharField(max_length=254)),
                ('nature', models.CharField(max_length=254)),
                ('zone', models.CharField(max_length=254)),
                ('nb_village', models.BigIntegerField()),
                ('altitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]