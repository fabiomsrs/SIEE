from django.conf.urls import url

from aluno import views

urlpatterns = [
    url('^my_curriculum/$', views.my_curriculum, name="my_curriculum"),
    url('^student_home/$', views.student_home, name="student_home"),
    url('^search_by_vacancies/$', views.search_by_vacancies, name="search_by_vacancies")

]