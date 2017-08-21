from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core import validators
import re
from django.db import models
from enumfields import EnumField
from enumfields import Enum

# Create your models here.

class Usuario(AbstractBaseUser):

    TIPO_USUARIO = (('aluno', 'ALUNO'),
                    ('admin', 'ADMIN'))


    username = models.CharField('Nome do Usuário', max_length=30, unique=True, validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                                                                     'O nome do user so pode conter letras, digitos ou os''seguintes caracteres @/./+/-/_'
                                                                                                                     'invalid')])
    nome = models.CharField('Nome', max_length=100, blank=False)
    email = models.EmailField('E-mail', unique=True)
    tipo_usuario = models.CharField("Tipo Usuario", max_length=255, blank=True, null=True, choices=TIPO_USUARIO, default='Aluno')
    user_curriculo = models.ForeignKey('aluno.CurriculoAluno', related_name='user_curriculo', null=True)

    class Meta:
        verbose_name = 'Usuário'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = UserManager()


#TODO SIEE class and Ficha de supervisão

