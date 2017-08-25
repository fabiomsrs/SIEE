from django.db import models

# Create your models here.

class CurriculoAluno(models.Model):

    ESTADO_CIVIL = (('solteiro', 'SOLTEIRO'),
                    ('casado', 'CASADO'),
                    ('divorciado', 'DIVORCIADO'))

    SERIE = (('ensino_medio', 'ENSINO MEDIO'),
                    ('ensino_superior', 'ENSINO SUPERIOR'),
                    ('tecnico', 'TECNINO'))

    # ATIVO = (('ativo', 'ATIVO'),
    #          ('inativo', 'INATIVO'))

    nome = models.CharField("Nome Completo", max_length=255, null=False)
    email = models.CharField("Email", max_length=255, null=False)
    telefone = models.IntegerField("Telefone", null=True)
    matricula = models.CharField("Matricula", max_length=255, null=True)
    rg = models.IntegerField("RG", null=True)
    cpf = models.IntegerField("CPF", null=True)
    data_nascimento = models.DateField("Data Nascimento", blank=True, null=True)
    endereco = models.CharField("Endereço", max_length=255, null=True)
    estado_civil = models.CharField("Estado Civil", max_length=255, blank=True, null=True, choices=ESTADO_CIVIL)
    serie = models.CharField("Serie", max_length=255, blank=True, null=True, choices=SERIE)
    experiencia_profissional = models.CharField("Experiencia Profissional", max_length=255, null=True)
    objetivo = models.CharField("Objetivos", max_length=255, null=True)
    cursos_extras = models.CharField("Cursos Extras", max_length=255, null=True)
    formacao_academica = models.CharField("Formação Academica", max_length=255, null=True)
    participacao_eventos = models.CharField("Participação em Eventos", max_length=255, null=True)
    # curriculo_ativo = models.CharField("Curriculo Ativo", max_length=255, blank=True, null=True, choices=ATIVO, default='inativo')