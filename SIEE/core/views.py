from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from aluno.models import CurriculoAluno
from config import settings
from core.forms import *

from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.views.generic import View

from core.utils import render_to_pdf

from aluno.forms import RegisterMyCurriculum

from core.models import Usuario

User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def institution_area(request):
#     return render(request, 'login_user.html')

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


@login_required
def institution_home(request):
    template_name = 'user_home.html'
    return render(request, template_name)


def institution_area(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'aluno'in request.user.tipo_usuario:
                print('ALUNO')
                return redirect(settings.STUDENT_HOME)
            if 'admin' in request.user.tipo_usuario:
                print('ADMIN')
                return redirect(settings.INSTITUTION_HOME)
            else:
                print('nao encontrou nada')
                return HttpResponse("<h1>LOGIN ERROR</h1>")
        else:
            return HttpResponse("<h1>LOGIN ERROR</h1>")
    else:
        form = AuthenticationForm()
        return render(request, "login_user.html", {'form' : form} )


@login_required
def student_registration(request):
    template_name = 'student_registration.html'
    context = {'alunos' : CurriculoAluno.objects.all()}
    return render(request, template_name, context)

def detail_register_student(request, student_id):
    template_name = 'detail_register_student.html'
    context = {'student' : CurriculoAluno.objects.get(id=student_id)}
    return render(request, template_name, context)

def data_reports(request):
    template_name = 'data_reports.html'
    return render(request, template_name)

class GeneratePdfReportsUser(View):

    def get(self, request, *args, **kwargs):
        template = get_template('report/report_user.html')
        context = {
            'students' : CurriculoAluno.objects.all()
        }
        html = template.render(context)

        pdf = render_to_pdf('report/report_user.html', context)
        if pdf:
            reponse = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" % (filename)

            download = request.GET.get("download")
            if download:
                content = "attachement; filename='%s'" % (filename)
            reponse['Content-Disposition'] = content
            return reponse
        return  HttpResponse("Not Found")
