from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render


# Create your views here.
def index(request):
    contexto={
        
    }
    return render(request,"index.html",contexto)

def aluno(request):
    return render(request,"aluno.html")

def professor(request):
    return render(request,"professor.html")

def disciplina(request):
    return render(request,"disciplina.html")

def detalhe_curso(request):
    return render(request,"detalhe_curso.html")

def lista_cursos(request):
    contexto={
        "cursos":Curso.objects.all()
    }
    return render(request,"lista_cursos.html",contexto)

def noticias(request):
    return render(request,"noticias.html")

def contato(request):
    if request.POST:
        form = ContactForm(request.POST)
        #form.enviar_email()
    else:
        form = ContactForm(request.POST)
    contexto = {
        "form":form
    }
    return render(request,"contato.html",contexto)

def login(request):
    return render(request,"login.html")

def logout(request, *args, **kwargs):
    kwargs['next_page'] = reverse('')
    return logout(request, *args, **kwargs)

def checa_aluno(user):
     return user.perfil == 'A'

def checa_professor(user):
     return user.perfil == 'P'



# Funções de teste…
@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?error=acesso', redirect_field_name=aluno)
def aluno(request):
     return render(request,"aluno.html")
@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=professor)
@login_required(login_url='/entrar')
def professor(request):
     return render(request,"professor.html")



