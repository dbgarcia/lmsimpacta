"""lmsimpacta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import *
from django.contrib.auth.views import login,logout,password_change,password_change_done
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index, name="home"),
    url(r'disciplina',disciplina),
    url(r'detalhe_curso',detalhe_curso),
    url(r'index',index),
    url(r'noticias',noticias),
    url(r'lista_curso',lista_cursos),
    url(r'contato',contato),
    url(r'entrar',login,{"template_name":"login.html"},name="login"),
    url(r'sair',logout,{"template_name":"logout.html"}),
    url(r'aluno',aluno),
    url(r'professor',professor),
    url(r'^restrito/$',restrito,name="restrito"),
    url(r'permission',permission),
    url(r'^restrito/questao',questao_form,name="questao_form"),

    url(r'^accounts/password/change/$', password_change, {
        'template_name': 'registration/password_change_form.html'}, 
        name='password_change'),
    url(r'^accounts/password/change/done/$', password_change_done, 
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)