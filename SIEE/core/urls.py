from django.conf.urls import url,include
from django.contrib.auth.views import login, logout, logout_then_login

from core import views

urlpatterns = [
    url('^$', views.index, name='index'),
    # url('^institution_area/$', views.institution_area, name="institution_area"),
    url('^register_user/$', views.register_user, name="register_user"),
    url('^institution_home/$', views.institution_home, name="institution_home"),
    url('^list_companies/$', views.list_companies, name="list_companies"),
    url('^list_vacancies/$', views.list_vacancies, name="list_vacancies"),
    url('^register_company/$', views.register_company, name="register_company"),
    url('^register_vacancy/$', views.register_vacancy, name="register_vacancy"),
    url('^register_student/$', views.register_student, name="register_student"),
    url('^student_home/$', views.student_home, name="student_home"),
    url('^my_curriculum/$', views.my_curriculum, name="my_curriculum"),


    url('^student_area/$', views.student_area, name="login_student"),




    # url('^student_area/$', views.student_area, name='student_area'),

    # url('^student_area/$', login, {'template_name': 'student_area.html'}, name='login_student'),
    url('^institution_area/$', login, {'template_name': 'institution_area.html'}, name='login_institution'),

    url('^logout/', logout_then_login, {'login_url' : 'index'}, name='logout_usuario'),
    url('^logout/', logout_then_login, {'login_url' : 'login_student'}, name='logout_student') #so pra encher linguiça
]

