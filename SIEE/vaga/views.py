from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from aluno.models import CurriculoAluno
from config import settings
from vaga.forms import *

# Create your views here.

@login_required
def register_company(request):
    template_name = 'register_company.html'
    if request.method == 'POST':
        form_register_company = RegisterCompanyForm(request.POST)

        if form_register_company.is_valid():
            company = form_register_company.save(commit=False)
            company.save()
            form_register_company = RegisterCompanyForm()
            return redirect(settings.LISTA_COMPANY)
    else:
        form_register_company = RegisterCompanyForm()
    context = {'form_register_company' : form_register_company}

    return render(request, template_name, context)

@login_required
def list_companies(request):
    template_name = 'list_companies.html'
    context = {'empresas' : Empresa.objects.all()}
    return render(request, template_name, context)

@login_required
def register_vacancy(request):
    template_name = 'register_vacancy.html'
    if request.method == 'POST':
        form_register_vacancy = RegisterVacancyForm(request.POST)

        if form_register_vacancy.is_valid():
            vacancy = form_register_vacancy.save(commit=False)
            vacancy.save()
            form_register_vacancy = RegisterVacancyForm()
            return redirect(settings.LISTA_VAGA)

    else:
        form_register_vacancy = RegisterVacancyForm()

    context = {'form_register_vacancy' : form_register_vacancy}
    return render(request, template_name, context)

@login_required
def register_area(request):
    template_name = 'register_area.html'
    if request.method == 'POST':
        form_register_course = RegisterCourseForm(request.POST)

        if form_register_course.is_valid():
            course = form_register_course.save(commit=False)
            course.save()
            return redirect(settings.INSTITUTION_HOME)
    else:
        form_register_course = RegisterCourseForm(request.POST)

    context = {'form_register_course' : form_register_course}
    return render(request, template_name, context)

@login_required
def list_vacancies(request):
    template_name = 'list_vacancies.html'
    context = {'vagas' : Vaga.objects.all()}
    return render(request, template_name, context)

@login_required
def student_registration(request):
    template_name = 'student_registration.html'
    context = {'alunos' : CurriculoAluno.objects.all()}
    return render(request, template_name, context)
