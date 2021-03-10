from django.contrib import admin
from .models import Aluno, Escola, Serie, TipoSerie, Turma

admin.site.register(Escola)
admin.site.register(Serie)
admin.site.register(TipoSerie)


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'pai', 'mae', 'turma']
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