from django import forms
from django.core.mail import send_mail

from config import settings
from vaga.models import Empresa, Vaga, AreaAtuacao


class RegisterCompanyForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class RegisterVacancyForm(forms.ModelForm):
    data_inicio = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False)

    class Meta:
        model = Vaga
        fields = '__all__'

class RegisterCourseForm(forms.ModelForm):
    class Meta:
        model = AreaAtuacao
        fields = '__all__'
