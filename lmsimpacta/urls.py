
from django.conf.urls import url
from django.contrib import admin
from core.views import *
from django.contrib.auth.views import login,logout

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
]