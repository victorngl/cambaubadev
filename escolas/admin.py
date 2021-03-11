from django.contrib import admin
from .models import Aluno, Escola, Serie, TipoSerie, Turma


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'serie']
    autocomplete_fields = ['serie']
    search_fields = ['nome']


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'pai', 'mae', 'turma', 'usuario_criacao', 'usuario_atualizacao']
    list_filter = ['pai', 'mae', 'turma', 'turma__serie']
    autocomplete_fields = ['turma', 'pai', 'mae']
    search_fields = ['nome', 'pai__username', 'mae__username']
    fieldsets = (
        ('Dados Principais', {'fields': (
			'nome',
			'cpf_cnpj',
			'rg',
			'pai',
            'mae'
		)}),
        ('Contatos', {'fields': (
			'telefone',
			'celular',
			'email',
		)}),
        ('Dados Adicionais', {'fields': (
			'turma',
			'observacao',
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