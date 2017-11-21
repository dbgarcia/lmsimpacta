from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Curso, Aluno, Professor, Disciplina
from django import forms

class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra','email', 'nome','curso')

    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'A'
        if commit:
            user.save()
        return user

class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('email', 'nome', 'curso')

class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome','email','curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'nome', 'email', 'curso')}),)
    add_fieldsets = (
        (None, {
             'fields': ('ra', 'nome', 'email', 'curso')
            }),
    )
    search_fields = ('ra',)
    ordering = ('nome',)
    filter_horizontal = ()

class NovoProfForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('ra','nome', 'email', 'celular', 'apelido')
            
    def save(self, commit=True):
        user = super(NovoProfForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'P'
        if commit:
            user.save()
        return user

class AlterarProfForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('email', 'nome', 'apelido','celular')

class ProfAdmin(UserAdmin):
    form = AlterarProfForm
    add_form = NovoProfForm
    list_display = ('ra', 'nome','email','celular','apelido')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'nome', 'email', 'celular','apelido')}),)
    add_fieldsets = (
        (None, {
             'fields': ('ra', 'nome', 'email', 'apelido','celular')
            }),
    )
    search_fields = ('ra',)
    ordering = ('nome',)
    filter_horizontal = ()

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','tipo','carga_horaria')
    list_filter = ('tipo',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome','curso')
    list_filter = ('nome',)

# Register your models here.

admin.site.register(Professor, ProfAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)