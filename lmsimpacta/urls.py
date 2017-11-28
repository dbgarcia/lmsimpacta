

from django.conf.urls import url
from django.contrib import admin
from core.views import *
from django.conf import settings		
from django.conf.urls.static import static
from django.contrib.auth.views import login,logout,password_change,password_change_done

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
    url(r'aluno', aluno),
    url(r'professor',professor),
    url(r'boletim',boletim),
    url(r'permission',permission),



    url(r'^accounts/password/change/$', password_change, {
        'template_name': 'registration/password_change_form.html'}, 
        name='password_change'),
    url(r'^accounts/password/change/done/$', password_change_done, 
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
