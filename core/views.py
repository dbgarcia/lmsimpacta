from django.shortcuts import render
from .forms import ContatoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from core.models import Curso,Usuario,Disciplina
from core.forms import ContatoForm,CursoForm

# Create your views here.
def index(request):
    contexto={
        #"usuario":Usuario.objects.all()
        #"usuario":{{ usuario.nome }},
        #aluno,professor,sbruble
        #"perfil":"aluno",
    }
    return render(request,"index.html",contexto)

def disciplina(request):
    contexto={
        "cursos":Curso.objects.all()
    }
    return render(request,"disciplina.html",contexto)

def detalhe_curso(request):
    contexto={
        "cursos" : Curso.objects.all(),
        "disciplina" : Disciplina.objects.all()
    }
    return render(request,"detalhe_curso.html",contexto)

def lista_cursos(request):
    contexto={
        "cursos":Curso.objects.all()
    }
    return render(request,"lista_cursos.html",contexto)

def noticias(request):
    return render(request,"noticias.html")

def contato(request):
    print(request.POST)
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.envia_email()
    else:
        form = ContatoForm()

    contexto = {
        "form":form
    }
    return render(request,"contato.html",contexto)

def login(request):
    return render(request,"login.html")

def curso(request):
    print(request.POST)
    if request.POST:
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoForm()

    contexto = {    
        "form":form
    }
    return render(request,"curso.html",contexto)


def checa_aluno(user):
     return user.perfil == 'A'

def checa_professor(user):
     return user.perfil == 'P'

@login_required(login_url='/login')
@user_passes_test(checa_aluno, login_url='/?error=acesso', redirect_field_name=None)
def aluno(request):
    return render(request,"aluno.html")

@login_required(login_url='/entrar')
@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
def professor(request):
     return render(request,"professor.html")
    
