from django.conf.urls import url,include
from django.contrib.auth.views import login, logout, logout_then_login

from core import views

urlpatterns = [
    url('^$', views.index, name='index'),
    # url('^institution_area/$', views.institution_area, name="institution_area"),
    url('^register_user/$', views.register_user, name="register_user"),
    url('^institution_home/$', views.institution_home, name="institution_home"),
    url('^institution_area/$', views.institution_area, name='login_institution'),
    url('^student_registration/$', views.student_registration, name='student_registration'),
    url('^student_registration/detail_register_student->(?P<student_id>\d+)$$', views.detail_register_student, name='detail_register_student'),

    url('^logout/', logout_then_login, {'login_url' : 'login_institution'}, name='logout_usuario'),
]

