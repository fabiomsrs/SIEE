# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_aluno_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.IntegerField(verbose_name='CPF'),
        ),
    ]
