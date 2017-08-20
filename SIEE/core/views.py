from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from config import settings
from core.forms import *

User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def institution_area(request):
#     return render(request, 'institution_area.html')

def register_user(request):
    template_name = 'register_user.html'
    # if request.method == 'POST':
    #     form_register_user = RegisterUser(request.POST)
    #
    #     if form_register_user.is_valid():
    #         user = form_register_user.save()
    #         user = authenticate(username=user.username, password=form_register_user.cleaned_data['senha1'])
    #         return redirect(settings.REGISTER_USER)
    #     else:
    #         return HttpResponse("<h1>CADASTRO ERROR</h1>")
    #
    # else:
    #     form_register_user = RegisterUser()

    if request.method == "POST":
        form_register_user = RegisterUser(request.POST)
        if form_register_user.is_valid():
            usuario = form_register_user.save(commit=False)
            usuario.save()
            return redirect(settings.REGISTER_USER)
        else:
            return HttpResponse("<h1>CADASTRO INVALIDO</h1>")
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


def register_course(request):
    template_name = 'register_course.html'
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


def student_home(request):
    template_name = 'student_home.html'
    return render(request, template_name)

def my_curriculum(request):
    template_name = 'my_curriculum.html'
    # aluno = Aluno.objects.all().filter(id=request.user.id)
    if request.method == 'POST':
        form_register_my_curriculum = RegisterMyCurriculum(request.POST)

        if form_register_my_curriculum.is_valid():
            curriculum = form_register_my_curriculum.save(commit=False)
            # aluno.curriculum = curriculum
            curriculum.save()
            return redirect(settings.REGISTER_CURRICULUM)
    else:
        form_register_my_curriculum = RegisterMyCurriculum(instance=request.user)

    context = {'form_register_my_curriculum' : form_register_my_curriculum}
    return render(request, template_name, context)


def list_vacancies(request):
    template_name = 'list_vacancies.html'
    context = {'vagas' : Vaga.objects.all()}
    return render(request, template_name, context)

def institution_area(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            if '1'in request.user.tipo_usuario:
                print('ALUNO')
                return redirect(settings.LOGIN_STUDENT)
            if '2' in request.user.tipo_usuario:
                print('ADMIN')
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                print('nao encontrou nada')
                return HttpResponse("<h1>LOGIN ERROR</h1>")
        else:
            return HttpResponse("<h1>LOGIN ERROR</h1>")
    else:
        form = AuthenticationForm()
        return render(request, "institution_area.html", {'form' : form} )

