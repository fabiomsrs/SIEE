from django.core.mail import send_mail

from aluno.models import CurriculoAluno
from django import forms

from config import settings


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

    data_nascimento = forms.DateField(label='Data Nascimento', widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False),

    class Meta:
        model = CurriculoAluno
        exclude = ['aluno', 'curriculo_ativo']
        fields = '__all__'


class ContactCompany(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', max_length=100, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                              required=False)

# def send_mail(self, company):
#     subject = '[%s] Contato' % company
#     message = 'Nome: %s(name)s;Email: %(email)s; %(message)s'
#     context = {
#         'name': self.cleaned_data['name'],
#         'email': self.cleaned_data['email'],
#         'message': self.cleaned_data['message']
#     }
#
#     message = message % context
#     send_mail(
#         subject, message, settings.DEFAULT_FROM_EMAIL,
#               [settings.CONTACT_EMAIL]
#     )



class SearchByVacancies(forms.Form):
    pass