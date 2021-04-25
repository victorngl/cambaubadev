from django.contrib import admin
from .models import Aluno, Escola, Serie, TipoSerie, Turma, Materia, Professor


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'serie']
    autocomplete_fields = ['serie']
    filter_horizontal = ['professores']
    search_fields = ['nome']


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'responsavel1', 'responsavel2', 'responsavel3', 'turma']
    list_filter = ['responsavel1', 'responsavel2', 'responsavel3', 'turma', 'turma__serie']
    autocomplete_fields = ['turma', 'usuario', 'responsavel1', 'responsavel2', 'responsavel3']
    search_fields = ['nome', 'responsavel1__username', 'responsavel2__username', 'responsavel3__username']
    fieldsets = (
        ('Dados Principais', {'fields': (
			'nome',
			'cpf_cnpj',
			'rg',
			'usuario',
			'responsavel1',
			'responsavel2',
			'responsavel3'
		)}),
        ('Contatos', {'fields': (
			'telefone',
			'celular',
			'email',
		)}),
        ('Dados Adicionais', {'fields': (
			'turma',
			'observacao',
            'foto',
		)}),
    )

@admin.register(Escola)
class EscolaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    
@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_filter = ['tipo_serie', 'escola']
    autocomplete_fields = ['tipo_serie', 'escola']
    search_fields = ['nome']

@admin.register(TipoSerie)
class TipoSerieAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo']
    search_fields = ['titulo']

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    fieldsets = (
        ('Dados Principais', {'fields': (
			'nome',
			'cpf_cnpj',
			'rg',
			'usuario',
		)}),
        ('Contatos', {'fields': (
			'telefone',
			'celular',
			'email',
		)})
    )