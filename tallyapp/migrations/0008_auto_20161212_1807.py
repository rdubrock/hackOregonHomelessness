# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 18:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0007_auto_20161212_0658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyhicapi',
            options={'ordering': ('Date', 'Table', 'Shelter', 'UnitBed')},
        ),
        migrations.AlterModelOptions(
            name='historypitsubpopulationsapi',
            options={'ordering': ('Date', 'Table', 'Population', 'Shelter')},
        ),
        migrations.AlterModelOptions(
            name='historypitsummaryapi',
            options={'ordering': ('Date', 'Table', 'Population', 'SubPopulation')},
        ),
    ]
