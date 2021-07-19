from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Aluno, Escola, Serie, TipoSerie, Turma, Materia, Professor, Responsavel


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'serie', 'email_pai_responsavel']
    autocomplete_fields = ['serie']
    filter_horizontal = ['professores']
    search_fields = ['nome']
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']


@admin.register(Aluno)
class AlunoAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nome', 'responsavel1', 'responsavel2', 'responsavel3', 'responsavel4', 'responsavel5', 'turma']
    list_filter = ['responsavel1', 'responsavel2', 'responsavel3', 'responsavel4', 'responsavel5', 'turma', 'turma__serie']
    autocomplete_fields = ['turma', 'usuario', 'responsavel1', 'responsavel2', 'responsavel3', 'responsavel4', 'responsavel5']
    search_fields = ['nome', 'responsavel1__username', 'responsavel2__username', 'responsavel3__username', 'responsavel4__username', 'responsavel5__username']
    fieldsets = (
        ('Dados Principais', {'fields': (
			'nome',
			'cpf_cnpj',
			'rg',
			'usuario',
			'responsavel1',
			'responsavel2',
			'responsavel3',
			'responsavel4',
			'responsavel5'
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
        ('Dados Extras', {'fields': (
			'matricula',
			'id_sigma',
            'username',
            'senha',
		)}),
    )

@admin.register(Escola)
class EscolaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']
    
@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_filter = ['tipo_serie', 'escola']
    autocomplete_fields = ['tipo_serie', 'escola']
    search_fields = ['nome']
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

@admin.register(TipoSerie)
class TipoSerieAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'foto_capa']
    search_fields = ['titulo']
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

@admin.register(Professor)
class ProfessorAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    autocomplete_fields = ['usuario']
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
		)}),
        ('Dados Extras', {'fields': (
			'id_acesso',
			'id_sigma',
			'username',
			'senha',
		)})
    )


@admin.register(Responsavel)
class responsavelAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    autocomplete_fields = ['usuario']
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
		)}),
        ('Dados Extras', {'fields': (
			'id_acesso',
			'id_sigma',
			'username',
			'senha',
		)})
    )