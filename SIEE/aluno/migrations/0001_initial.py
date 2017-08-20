# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurriculoAluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('matricula', models.CharField(max_length=255, verbose_name='Matricula')),
                ('rg', models.IntegerField(verbose_name='RG')),
                ('cpf', models.IntegerField(verbose_name='CPF')),
                ('data_nascimento', models.DateField(blank=True, verbose_name='Data Nascimento')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('estado_civil', models.CharField(blank=True, choices=[('solteiro', 'SOLTEIRO'), ('casado', 'CASADO'), ('divorciado', 'DIVORCIADO')], max_length=255, null=True, verbose_name='Estado Civil')),
                ('experiencia_profissional', models.CharField(max_length=255, null=True, verbose_name='Experiencia Profissional')),
                ('cursos_extras', models.CharField(max_length=255, null=True, verbose_name='Cursos Extras')),
                ('formacao_academica', models.CharField(max_length=255, null=True, verbose_name='Formação Academica')),
                ('participacao_eventos', models.CharField(max_length=255, null=True, verbose_name='Participação em Eventos')),
            ],
        ),
    ]
