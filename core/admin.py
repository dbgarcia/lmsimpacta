from django.contrib import admin
from django import forms
from core.models import Curso,Aluno
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


# Register your models here.
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Curso,CursoAdmin)
