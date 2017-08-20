from django.conf.urls import url

from vaga import views

urlpatterns = [
    url('^list_companies/$', views.list_companies, name="list_companies"),
    url('^list_vacancies/$', views.list_vacancies, name="list_vacancies"),
    url('^register_company/$', views.register_company, name="register_company"),
    url('^register_vacancy/$', views.register_vacancy, name="register_vacancy"),
    url('^register_course/$', views.register_course, name="register_course"), #alterar classe
]