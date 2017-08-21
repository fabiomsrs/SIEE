from django.db import models

# Create your models here.


class AreaAtuacao(models.Model):
    nome = models.CharField("Area Atuacao",max_length=255, null=False)
    area = models.CharField("Descrição",max_length=255)

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

    TIPO_VAGA =     (('estagio', 'ESTAGIO'),
                    ('emprego', 'EMPREGO'),
                     ('jovem aprendiz', 'JOVEM APRENDIZ'))

    TURNO_VAGA =    (('manha', 'MANHA'),
                    ('tarde', 'TARDE'),
                     ('noite', 'NOITE'))

    STATUS_VAGA = (('ativo', 'ATIVO'),
                   ('inativo', 'INATIVO'))

    area_atuacao = models.CharField('Area de Atuação', max_length=255, blank=False)
    cargo = models.CharField('Cargo', max_length=100, blank=False)
    quantidade = models.IntegerField("Quantidade de Vagas", null=False)
    tipo_vaga = models.CharField('Tipo Vaga', max_length=255, choices=TIPO_VAGA)
    beneficios = models.CharField('Beneficios', max_length=255, blank=False)
    requisitos = models.CharField('Requisitos', max_length=255, blank=False)
    atividades = models.CharField('Atividades', max_length=255, blank=False)
    valor = models.DecimalField("Valor", max_digits=15, decimal_places=2, default=0)
    turno = models.CharField('Turno Vaga', max_length=255, choices=TURNO_VAGA)
    status = models.CharField('Status Vaga', max_length=255, choices=STATUS_VAGA, default='ativo')
    area_atuacao = models.ForeignKey('vaga.AreaAtuacao', related_name='curso_vaga')
    empresa_vaga = models.ForeignKey('vaga.Empresa', related_name='empresa_vaga')