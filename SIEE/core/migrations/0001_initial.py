# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 23:24
from __future__ import unicode_literals

import core.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome do user so pode conter letras, digitos ou osseguintes caracteres @/./+/-/_invalid')], verbose_name='Nome do Usuário')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('tipo_usuario', enumfields.fields.EnumField(default='aluno', enum=core.models.TipoUsuario, max_length=255)),
            ],
            options={
                'verbose_name': 'Usuário',
            },
        ),
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
                ('estado_civil', enumfields.fields.EnumField(default='solteiro', enum=core.models.EstadoCivil, max_length=255)),
                ('experiencia_profissional', models.CharField(max_length=255, null=True, verbose_name='Experiencia Profissional')),
                ('cursos_extras', models.CharField(max_length=255, null=True, verbose_name='Cursos Extras')),
                ('formacao_academica', models.CharField(max_length=255, null=True, verbose_name='Formação Academica')),
                ('participacao_eventos', models.CharField(max_length=255, null=True, verbose_name='Participação em Eventos')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome Curso')),
                ('area', models.CharField(max_length=255, verbose_name='Area de Atuação')),
                ('turno_aulas', models.CharField(max_length=255, verbose_name='Turno')),
                ('cordenador_curso', models.CharField(max_length=255, verbose_name='Cordenador')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade de Vagas')),
                ('tipo_vaga', enumfields.fields.EnumField(default='estagio', enum=core.models.TipoVaga, max_length=255)),
                ('data_inicio', models.DateField(blank=True, verbose_name='Data inicio')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Valor')),
                ('turno', enumfields.fields.EnumField(default='tarde', enum=core.models.TurnoVaga, max_length=255)),
                ('curso_vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso_vaga', to='core.Curso')),
                ('empresa_vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_vaga', to='core.Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='curriculoaluno',
            name='curso_aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso_aluno', to='core.Curso'),
        ),
    ]
