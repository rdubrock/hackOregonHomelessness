# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0003_auto_20161211_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='PitSubpopulationsAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Table', models.CharField(default='', max_length=17, null=True)),
                ('Population', models.CharField(default='', max_length=67, null=True)),
                ('Shelter', models.CharField(default='', max_length=40, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Value', models.DecimalField(decimal_places=7, max_digits=7, null=True)),
            ],
            options={
                'ordering': ('Table', 'Population', 'Shelter', 'Date'),
            },
        ),
        migrations.AlterModelOptions(
            name='historyhicapi',
            options={'ordering': ('Table', 'Shelter', 'UnitBed', 'Date')},
        ),
        migrations.AlterModelOptions(
            name='historypitsummaryapi',
            options={'ordering': ('Table', 'Population', 'SubPopulation', 'Date')},
        ),
        migrations.RemoveField(
            model_name='historyhicapi',
            name='BedType',
        ),
        migrations.AddField(
            model_name='historyhicapi',
            name='Table',
            field=models.CharField(default='', max_length=23, null=True),
        ),
        migrations.AddField(
            model_name='historyhicapi',
            name='UnitBed',
            field=models.CharField(default='', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='historyhicapi',
            name='Value',
            field=models.DecimalField(decimal_places=7, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='historyhicapi',
            name='Shelter',
            field=models.CharField(default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='historypitsummaryapi',
            name='Population',
            field=models.CharField(default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='historypitsummaryapi',
            name='SubPopulation',
            field=models.CharField(default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='historypitsummaryapi',
            name='Value',
            field=models.DecimalField(decimal_places=7, max_digits=7, null=True),
        ),
    ]