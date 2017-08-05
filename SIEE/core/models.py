from django.db import models
from enumfields import EnumField
from enumfields import Enum
# Create your models here.

class TipoVaga(Enum):
	EMPREGO = 'emprego'
	JOVEM_APRENDIZ = 'jovem aprendiz'
	ESTAGIO = 'estagio'
	DEFAULT = 'DEFAULT'

class Ifpi(models.Model):
	nome_ifpi = models.CharField(max_length=25)
	curso = models.ManyToManyField('Curso', verbose_name='lista de cursos')
	
	def __str__(self):
		return nome_ifpi

class Curso(models.Model):
	nome_curso = models.CharField(max_length=25)
	area_curso = models.CharField(max_length=25)
	oferta_de_vaga = models.ManyToManyField('OfertaDeVaga', verbose_name='oferta de vagas')
	
	def __str__(self):
		return nome_curso

class Responsavel(models.Model):
	nome_responsavel = models.CharField(max_length=45)

class Vaga(models.Model):
	responsavel = models.ForeignKey('Responsavel', related_name='vagas_responsaveis')
	oferta_de_vaga = models.ForeignKey('OfertaDeVaga', on_delete=models.CASCADE)

class OfertaDeVaga(models.Model):
	tipo_vaga = EnumField(TipoVaga,max_length=25, default=TipoVaga.DEFAULT)
	aluno = models.ManyToManyField('Aluno', through='CartaDeEncaminhamento')

class CartaDeEncaminhamento(models.Model):
	oferta_de_vaga = models.ForeignKey('OfertaDeVaga')
	aluno = models.ForeignKey('Aluno')

class Aluno(models.Model):
	matricula = models.CharField(max_length=10) #chave candidata
	nome_aluno = models.CharField(max_length=45)

class TermoDeCompromisso(models.Model):
	vaga = models.ForeignKey('Vaga',related_name='minhas_vagas')
	regras_do_compromisso = models.CharField(max_length=250)
	periodo = models.OneToOneField('Periodo')
	local_atuacao = models.ForeignKey('Empresa', related_name='meus_termos_de_compromisso')
	remuneracao = models.FloatField()
	apolice_de_seguro = models.IntegerField()

class Periodo(models.Model):
	data_inicio = models.DateTimeField(auto_now_add=True, blank=True)
	data_final = models.DateTimeField(blank=True)

class Empresa(models.Model):
	nome_empresa = models.CharField(max_length=25)

class TermoConvenho(models.Model):
	regras_do_convenho = models.CharField(max_length=250)

#TODO SIEE class and Ficha de supervisão

