from django.db import models

# Create your models here.

class CurriculoAluno(models.Model):

    ESTADO_CIVIL = (('solteiro', 'SOLTEIRO'),
                    ('casado', 'CASADO'),
                    ('divorciado', 'DIVORCIADO'))

    nome = models.CharField("Nome Completo", max_length=255, null=False)
    email = models.CharField("Email", max_length=255, null=False)
    matricula = models.CharField("Matricula", max_length=255, null=False)
    rg = models.IntegerField("RG", null=False)
    cpf = models.IntegerField("CPF", null=False)
    data_nascimento = models.DateField("Data Nascimento", blank=True, null=False)
    endereco = models.CharField("Endereço", max_length=255, null=False)
    estado_civil = models.CharField("Estado Civil", max_length=255, blank=True, null=True, choices=ESTADO_CIVIL)
    experiencia_profissional = models.CharField("Experiencia Profissional", max_length=255, null=True)
    cursos_extras = models.CharField("Cursos Extras", max_length=255, null=True)
    formacao_academica = models.CharField("Formação Academica", max_length=255, null=True)
    participacao_eventos = models.CharField("Participação em Eventos", max_length=255, null=True)