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