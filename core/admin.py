from django.contrib import admin
from django import forms
from core.models import Curso,Aluno,Professor,Disciplina,GradeCurricular,Periodo,PeriodoDisciplina,DisciplinaOfertada,Turma,Matricula,CursoTurma,Questao,ArquivoQuestao
from django.contrib.auth.admin import UserAdmin

class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra','nome', 'curso','celular', 'email')

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
    list_display = ('ra','nome', 'curso','celular', 'email')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra','nome', 'curso','celular', 'email')}),)
    add_fieldsets = (
        (None, {
             'fields': ('ra','nome', 'curso','celular', 'email')
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
        fields = ('ra','nome','apelido', 'email', 'celular')
            
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
        fields = ('ra','nome','apelido', 'email', 'celular')

class ProfAdmin(UserAdmin):
    form = AlterarProfForm
    add_form = NovoProfForm
    list_display = ('ra','nome','apelido', 'email', 'celular')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra','nome','apelido', 'email', 'celular')}),)
    add_fieldsets = (
        (None, {
             'fields': ('ra','nome','apelido', 'email', 'celular')
            }),
    )
    search_fields = ('ra',)
    ordering = ('nome',)
    filter_horizontal = ()

class GradeCurricularAdmin(admin.ModelAdmin):
    list_display = ('ano', 'curso', 'semestre')
    list_filter = ('ano','semestre', 'curso')
    ordering = ('ano',)
    
    

class DisciplinaAdmin(admin.ModelAdmin):
    list_display =('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)
    

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    list_filter = ('numero',)
    ordering = ('numero',)

class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ('ano',)
    list_filter = ('ano',)
    ordering = ('ano',)
   
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turno', 'ano', 'semestre',)
    list_filter = ('turno', 'ano', 'semestre',)
    ordering = ('turno', 'ano', 'semestre',)

class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'data_limite_entrega', 'descricao', 'data',)
    list_filter = ('numero', 'data_limite_entrega', 'descricao', 'data',)
    ordering = ('numero', 'data_limite_entrega', 'descricao', 'data',)  

class ArquivoQuestaoAdmin(admin.ModelAdmin):
    list_display = ('arquivo',)
    list_filter = ('arquivo',)
    ordering = ('arquivo',)
 
   
# Register your models here.  
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Professor,ProfAdmin)
admin.site.register(GradeCurricular,GradeCurricularAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(Periodo,PeriodoAdmin)
admin.site.register(PeriodoDisciplina)
admin.site.register(DisciplinaOfertada, DisciplinaOfertadaAdmin)
admin.site.register(Turma,TurmaAdmin)
admin.site.register(Matricula)
admin.site.register(CursoTurma)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(ArquivoQuestao,ArquivoQuestaoAdmin)