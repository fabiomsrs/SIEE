from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from django.core.mail import EmailMessage

from aluno.utils import render_to_pdf  # created in step 4

from config import settings
from aluno.forms import *

# Create your views here.
from vaga.models import Vaga, Empresa


def my_curriculum(request):
    template_name = 'my_curriculum.html'
    # aluno = Aluno.objects.all().filter(id=request.user.id)
    if request.method == 'POST':
        form_register_my_curriculum = RegisterMyCurriculum(request.POST, instance=request.user.user_curriculo)

        if form_register_my_curriculum.is_valid():
            curriculum = form_register_my_curriculum.save(commit=False)
            curriculum.save()
            request.user.add_curriculum(curriculum)
            return redirect(settings.STUDENT_HOME)
    else:
        form_register_my_curriculum = RegisterMyCurriculum(instance=request.user.user_curriculo)

    context = {'form_register_my_curriculum' : form_register_my_curriculum}
    return render(request, template_name, context)

def student_home(request):
    template_name = 'student_home.html'
    return render(request, template_name)

def search_by_vacancies(request):
    template_name = 'search_by_vacancies.html'
    context = {'vagas' : Vaga.objects.all()}
    return render(request, template_name, context)

def detail_vacancy(request, vacancy_id):
    template_name = 'detail_vacancy.html'
    context = {'vaga' : Vaga.objects.get(id=vacancy_id)}
    return render(request, template_name, context)


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf_curriculo.html')
        context = {
            # "nome_id": request.user.user_curriculo.email,
            "nome": request.user.nome,
            "telefone" : request.user.user_curriculo.telefone,
            "email": request.user.email,
            "rg": request.user.user_curriculo.rg,
            "endereco": request.user.user_curriculo.endereco,
            "cpf": request.user.user_curriculo.cpf,
            "objetivo": request.user.user_curriculo.objetivo,
            "data_nascimento": request.user.user_curriculo.data_nascimento,
            "escolaridade": request.user.user_curriculo.escolaridade,
            "formacao_academica": request.user.user_curriculo.formacao_academica,
            "cursos_extras": request.user.user_curriculo.cursos_extras,
            "experiencia_profissional": request.user.user_curriculo.experiencia_profissional,
            "participacao_eventos": request.user.user_curriculo.participacao_eventos,
        }
        html = template.render(context)

        pdf = render_to_pdf('pdf_curriculo.html', context)
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

@login_required
def send_mail(request, company_id):
    template_name = 'send_mail.html'
    # context ={}

    if request.method == 'POST':
        form = ContactCompanyForm(request.POST)
        if form.is_valid():
            empresa = Empresa.objects.get(id=company_id)
            # handle_uploaded_file(request.FILE['file'])
            email = EmailMessage(form.cleaned_data['nome'] + ' Solicitacao de Estagio from SIEE', form.cleaned_data['message'] + '\nSegue link para curriculo', to=[empresa.email])
            email.send()
            return redirect(settings.SEND_MAIL)
    else:
        form = ContactCompanyForm()

    context = {'form' : form,
               'company' : Empresa.objects.get(id=company_id)}
    # context['company'] = company
    return render(request, template_name, context)



