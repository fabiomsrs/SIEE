from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core import validators
import re
from django.db import models
from enumfields import EnumField
from enumfields import Enum

# Create your models here.

class TipoVaga(Enum):
    EMPREGO = 'emprego'
    JOVEM_APRENDIZ = 'jovem aprendiz'
    ESTAGIO = 'estagio'

class TurnoVaga(Enum):
    NOITE = 'noite'
    DIA = 'dia'
    TARDE = 'tarde'

class EstadoCivil(Enum):
    CASADO = 'casado'
    SOLTEIRO = 'solteiro'


class Curso(models.Model):
    nome = models.CharField("Nome Curso",max_length=255, null=False)
    area = models.CharField("Area de Atuação",max_length=255)
    turno_aulas = models.CharField("Turno",max_length=255)
    cordenador_curso = models.CharField("Cordenador",max_length=255)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Vaga(models.Model):

    descricao = models.CharField('Descricao', max_length=100, blank=False)
    quantidade = models.IntegerField("Quantidade de Vagas", null=False)
    tipo_vaga = EnumField(TipoVaga, max_length=255, default=TipoVaga.ESTAGIO)
    data_inicio = models.DateField("Data inicio", blank=True, null=False)
    valor = models.DecimalField("Valor", max_digits=15, decimal_places=2, default=0)
    turno = EnumField(TurnoVaga, max_length=255, default=TurnoVaga.TARDE)
    curso_vaga = models.ForeignKey('Curso', related_name='curso_vaga')
    empresa_vaga = models.ForeignKey('Empresa', related_name='empresa_vaga')


class Usuario(AbstractBaseUser):

    username = models.CharField('Nome do Usuário', max_length=30, unique=True, validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                                                                     'O nome do user so pode conter letras, digitos ou os''seguintes caracteres @/./+/-/_'
                                                                                                                     'invalid')])
    email = models.EmailField('E-mail', unique=True)
    nome = models.CharField('Nome', max_length=100, blank=False)

    class Meta:
        verbose_name = 'Usuário'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = UserManager()

class Aluno(AbstractBaseUser):
    username = models.CharField('Nome do Usuário', max_length=30, unique=True,
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                      'O nome do user so pode conter letras, digitos ou os''seguintes caracteres @/./+/-/_'
                                                                      'invalid')])
    nome = models.CharField("Nome Completo", max_length=255, null=False)
    email = models.CharField("Email", max_length=255, null=False)
    matricula = models.CharField("Matricula",max_length=255, null=False)
    curso_aluno = models.ForeignKey("Curso", related_name='curso_aluno', null=False)
    curriculo = models.ForeignKey('CurriculoAluno', related_name='curriculo_aluno', null=True)

    class Meta:
        verbose_name = 'Aluno'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = UserManager()

class CurriculoAluno(models.Model):

    rg = models.IntegerField("RG", null=False)
    cpf = models.IntegerField("CPF", null=False)
    data_nascimento = models.DateField("Data Nascimento", blank=True, null=False)
    endereco = models.CharField("Endereço", max_length=255, null=False)
    estado_civil = EnumField(EstadoCivil, max_length=255, default=EstadoCivil.SOLTEIRO)
    experiencia_profissional = models.CharField("Experiencia Profissional", max_length=255, null=True)
    cursos_extras = models.CharField("Cursos Extras", max_length=255, null=True)
    formacao_academica = models.CharField("Formação Academica", max_length=255, null=True)
    participacao_eventos = models.CharField("Participação em Eventos", max_length=255, null=True)

#TODO SIEE class and Ficha de supervisão

