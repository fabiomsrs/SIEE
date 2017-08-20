from aluno.models import CurriculoAluno
from django import forms


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

    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False),

    class Meta:
        model = CurriculoAluno
        exclude = ['aluno']
        fields = '__all__'
