from django.contrib import admin
from django import forms
from core.models import Curso,Aluno,Professor,Disciplina
from django.contrib.auth.admin import UserAdmin

class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra', 'nome','curso')

    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit = False)
        user.set_password("123")
        user.perfil = "A"
        if commit:
            user.save()
        return user        

class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ( 'nome', 'curso')

class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra','nome', 'curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra','nome', 'curso')}),)
    add_fieldsets = (
        (None, {
             'fields': ('ra','nome', 'curso')
             }),
        )
    search_fields = ('ra',)
    ordering = ('ra',)
    filter_horizontal = ()

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','tipo','carga_horaria')
    list_filter = ('tipo',)

class NovoProfForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('ra','nome', 'email', 'disciplina')
            
    def save(self, commit=True):
        user = super(NovoProfForm, self).save(commit=False)
        user.set_password('123')
        user.perfil = 'P'
        if commit:
            user.save()
        return user

class AlterarProfForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('email', 'nome', 'disciplina','carga_horaria')

class ProfAdmin(UserAdmin):
    form = AlterarProfForm
    add_form = NovoProfForm
    list_display = ('ra', 'nome','email','disciplina','carga_horaria')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'nome', 'email', 'disciplina')}),)
    add_fieldsets = (
        (None, {
             'fields': ('ra', 'nome', 'email', 'disciplina','carga_horaria')
            }),
    )
    search_fields = ('ra',)
    ordering = ('nome',)
    filter_horizontal = ()

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome','curso')
    list_filter = ('nome',)


# Register your models here.
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Professor, ProfAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
