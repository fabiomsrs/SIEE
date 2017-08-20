from django.shortcuts import render, redirect

from config import settings
from aluno.forms import *

# Create your views here.
from vaga.models import Vaga


def my_curriculum(request):
    template_name = 'my_curriculum.html'
    # aluno = Aluno.objects.all().filter(id=request.user.id)
    if request.method == 'POST':
        form_register_my_curriculum = RegisterMyCurriculum(request.POST)

        if form_register_my_curriculum.is_valid():
            curriculum = form_register_my_curriculum.save(commit=False)
            # aluno.curriculum = curriculum
            curriculum.save()
            return redirect(settings.STUDENT_HOME)
    else:
        form_register_my_curriculum = RegisterMyCurriculum(instance=request.user)

    context = {'form_register_my_curriculum' : form_register_my_curriculum}
    return render(request, template_name, context)



def student_home(request):
    template_name = 'student_home.html'
    return render(request, template_name)

def search_by_vacancies(request):
    template_name = 'search_by_vacancies.html'
    context = {'vagas' : Vaga.objects.all()}
    return render(request, template_name, context)