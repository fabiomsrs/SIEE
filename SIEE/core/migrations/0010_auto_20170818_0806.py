# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170818_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('cpf', models.IntegerField(verbose_name='CPF')),
                ('matricula', models.CharField(max_length=255, verbose_name='Matricula')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('data_nascimento', models.DateField(blank=True, verbose_name='Data Nascimento')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='cordenador_curso',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='turno_aulas',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso_aluno', to='core.Curso'),
        ),
    ]
