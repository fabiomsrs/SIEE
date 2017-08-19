from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxSelectMultiple

from core.models import Empresa, Vaga, TipoVaga, Aluno, CurriculoAluno

User = get_user_model()

class RegisterUser(forms.ModelForm):

    senha1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Confirmacao de Senha', widget=forms.PasswordInput)

    def verificar_senha(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("A Confirmacao nao esta Correta")
        return senha2

    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)
        user.set_password(self.cleaned_data['senha1'])

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        # abstract = True
        fields = ['username','email','nome']

class RegisterCompanyForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = '__all__'

class RegisterVacancyForm(forms.ModelForm):


    tipo_vaga = forms.TypedChoiceField(choices=TipoVaga.choices(), coerce=str, required=False)
    data_inicio = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False)

    class Meta:
        model = Vaga
        fields = '__all__'

class RegisterStudentForm(forms.ModelForm):

    senha1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Confirmacao de Senha', widget=forms.PasswordInput)

    def verificar_senha(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("A Confirmacao nao esta Correta")
        return senha2

    def save(self, commit=True):
        student = super(RegisterStudentForm, self).save(commit=False)
        student.set_password(self.cleaned_data['senha1'])

        student.email = self.cleaned_data['email']
        if commit:
            student.save()
        return student

    class Meta:
        model = Aluno
        fields = ['username', 'email', 'nome','matricula', 'curso_aluno']

class RegisterMyCurriculum(forms.ModelForm):

    experiencia_profissional = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),required=False)
    cursos_extras = forms.CharField(max_length=255,
                                               widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                                               required=False)
    formacao_academica = forms.CharField(max_length=255,
                                               widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                                               required=False)
    participacao_eventos = forms.CharField(max_length=255,
                                               widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                                               required=False)

    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False)

    class Meta:
        model = CurriculoAluno
        exclude = ['aluno']
        fields = '__all__'

