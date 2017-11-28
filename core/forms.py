# -*- coding: utf-8 -*-
from django import forms
from core.models import Curso,Questao,Matricula

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

class ContatoForm(forms.Form):

    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField()

    def envia_email(self):

        aluno = "Aluno: {0} \n".format(self.cleaned_data["nome"])
        email = "Email: {0} \n".format(self.cleaned_data["email"])
        mensagem = "Mensagem: {0} \n".format(self.cleaned_data["mensagem"])
        texto = "Email para você: {0} \n".format(self.cleaned_data["nome"])
        print("{0} {1} {2}, {3}".format(texto, aluno, email, mensagem))

class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        exclude = ['descricao']


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula



