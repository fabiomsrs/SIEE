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
    DEFAULT = 'default'

class Ifpi(models.Model):
    nome_ifpi = models.CharField(max_length=25)
    curso = models.ManyToManyField('Curso', verbose_name='lista de cursos')

class Curso(models.Model):
    nome = models.CharField(max_length=25)
    area = models.CharField(max_length=25)

class Empresa(models.Model):
    nome = models.CharField(max_length=25)
    descricao = models.CharField(max_length=25)
    endereco = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    telefone = models.CharField(max_length=25)

class Vaga(models.Model):
    curso_vaga = models.ForeignKey('Curso', related_name='curso_vaga')
    empresa_vaga = models.ForeignKey('Empresa', related_name='empresa_vaga')
    quantidade = models.IntegerField()
    tipo_vaga = EnumField(TipoVaga,max_length=25, default=TipoVaga.DEFAULT)
    data_inicio = models.DateTimeField(auto_now_add=True, blank=True)


class Usuario(AbstractBaseUser, PermissionsMixin):

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

#TODO SIEE class and Ficha de supervisão

