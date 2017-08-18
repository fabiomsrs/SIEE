from django.conf.urls import url,include
from django.contrib.auth.views import login, logout, logout_then_login

from core import views

urlpatterns = [
    url('^$', views.index, name='index'),
    # url('^institution_area/$', views.institution_area, name="institution_area"),
    url('^register_user/$', views.register_user, name="register_user"),
    url('^institution_home/$', views.institution_home, name="institution_home"),

    url('^institution_area/$', login, {'template_name': 'institution_area.html'}, name='login'),
    url('^logout/', logout_then_login, {'login_url' : 'login'}, name='logout_usuario')
]