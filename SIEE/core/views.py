from django.contrib.auth import authenticate, get_user_model, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from config import settings
from core.forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def institution_area(request):
#     return render(request, 'institution_area.html')

def register_user(request):
    template_name = 'register_user.html'
    if request.method == 'POST':
        form_register_user = RegisterUser(request.POST)

        if form_register_user.is_valid():
            user = form_register_user.save()
            user = authenticate(username=user.username, password=form_register_user.cleaned_data['senha1'])
            return redirect(settings.REGISTER_USER)
    else:
        form_register_user = RegisterUser()

    context = {'form_register_user': form_register_user}
    return render(request, template_name, context)

def institution_home(request):
    template_name = 'institution_home.html'
    return render(request, template_name)

def register_company(request):
    template_name = 'register_company.html'
    if request.method == 'POST':
        form_register_company = RegisterCompanyForm(request.POST)

        if form_register_company.is_valid():
            company = form_register_company.save(commit=False)
            company.save()
            form_register_company = RegisterCompanyForm()
            return redirect(settings.REGISTER_COMPANY)
    else:
        form_register_company = RegisterCompanyForm()
    context = {'form_register_company' : form_register_company}

    return render(request, template_name, context)

def list_companies(request):
    template_name = 'list_companies.html'
    context = {'empresas' : Empresa.objects.all()}
    return render(request, template_name, context)

def register_vacancy(request):
    template_name = 'register_vacancy.html'
    if request.method == 'POST':
        form_register_vacancy = RegisterVacancyForm(request.POST)

        if form_register_vacancy.is_valid():
            vacancy = form_register_vacancy.save(commit=False)
            vacancy.save()
            form_register_vacancy = RegisterVacancyForm()
            return redirect(settings.REGISTER_VAGA)

    else:
        form_register_vacancy = RegisterVacancyForm()

    context = {'form_register_vacancy' : form_register_vacancy}
    return render(request, template_name, context)

def list_vacancies(request):
    template_name = 'list_vacancies.html'
    context = {'vagas' : Vaga.objects.all()}
    return render(request, template_name, context)

def student_area(request):
    template_name = 'student_area.html'
    context = {'vagas' : Vaga.objects.all()}
    return render(request, template_name, context)