# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170818_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='quantidade',
            field=models.IntegerField(verbose_name='Quantidade de Vagas'),
        ),
    ]
