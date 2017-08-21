# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(blank=True, choices=[('aluno', 'ALUNO'), ('admin', 'ADMIN')], default='Aluno', max_length=255, null=True, verbose_name='Tipo Usuario'),
        ),
    ]