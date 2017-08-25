from urllib import request

from django.core.mail import send_mail

from aluno.models import CurriculoAluno
from django import forms

from config import settings
from django.core.mail import EmailMessage


class RegisterMyCurriculum(forms.ModelForm):

    experiencia_profissional = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),required=False)
    cursos_extras = forms.CharField(label='Cursos Extras',max_length=255,
                                    widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                                    required=False)
    formacao_academica = forms.CharField(label='Formação Academica' ,max_length=255,
                                         widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                                         required=False)
    participacao_eventos = forms.CharField(label='Participação em Eventos',max_length=255,
                                           widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                                           required=False)

    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False)

    class Meta:
        model = CurriculoAluno
        exclude = ['aluno', 'curriculo_ativo']
        fields = '__all__'


class ContactCompanyForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    # email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', max_length=100, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                              required=False)
    # file = forms.FileField(label='Anexe seu Curriculo', required=False)

    # def send_mail(self, empresa_email):
    #     email = EmailMessage('Solicitacao de Vaga de Estagio de ', 'message', to=[empresa_email])
    #     email.send()

class SearchByVacancies(forms.Form):
    pass