# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 00:31
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('object', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='curriculoaluno',
            name='curso_aluno',
        ),
    ]