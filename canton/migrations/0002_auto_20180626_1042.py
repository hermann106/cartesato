# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 10:42
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canton', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantons',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]
