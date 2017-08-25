from django.conf.urls import url

from aluno import views
from .views import GeneratePdf

urlpatterns = [
    url('^my_curriculum/$', views.my_curriculum, name="my_curriculum"),
    url('^student_home/$', views.student_home, name="student_home"),
    url('^search_by_vacancies/$', views.search_by_vacancies, name="search_by_vacancies"),
    url('^search_by_vacancies/send_mail/(?P<company_id>\d+)$', views.send_mail, name="send_mail"),
    url('^detail_vacancy/(?P<vacancy_id>\d+)$', views.detail_vacancy, name='detail_vacancy'),
    url('^pdf/$', GeneratePdf.as_view(), name='gerar_pdf'),


]