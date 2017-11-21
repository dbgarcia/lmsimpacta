from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def index(request):
    contexto={
        
    }
    return render(request,"index.html",contexto)



def disciplina(request):
    return render(request,"disciplina.html")

def detalhe_curso(request):
    return render(request,"detalhe_curso.html")

def lista_cursos(request):
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

#Checa

def checa_aluno(user):
     return user.perfil == 'A'

def checa_professor(user):
     return user.perfil == 'P'

#passtest

@login_required(login_url='/login')
@user_passes_test(checa_aluno, login_url='/?error=acesso', redirect_field_name=None)
def aluno(request):
     return render(request,"aluno.html")

@login_required(login_url='/login')
@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
def professor(request):
     return render(request,"professor.html")




