from django.contrib import admin
from .models import Oficina, AtividadeExtra, AtividadeNoturna, InscricaoOficina, InscricaoAtividadeExtra, InscricaoAtividadeNoturna


@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'vagas', 'data_inicial', 'data_final']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data_inicial', 'data_final']

@admin.register(AtividadeExtra)
class AtividadeExtraAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'vagas', 'data_inicial', 'data_final']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data_inicial', 'data_final']

@admin.register(AtividadeNoturna)
class AtividadeNoturnaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'vagas', 'data_inicial', 'data_final']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data_inicial', 'data_final']

@admin.register(InscricaoOficina)
class InscricaoOficinaAdmin(admin.ModelAdmin):
    list_display = ['oficina', 'aluno']
    list_filter = ['oficina', 'aluno']
    autocomplete_fields = ['oficina', 'aluno']
    fieldsets = (
        (None, {'fields': (
			'oficina',
			'aluno'
		)}),
    )

@admin.register(InscricaoAtividadeExtra)
class InscricaoAtividadeExtraAdmin(admin.ModelAdmin):
    list_display = ['oficina', 'aluno']
    list_filter = ['oficina', 'aluno']
    autocomplete_fields = ['oficina', 'aluno']
    fieldsets = (
        (None, {'fields': (
			'oficina',
			'aluno'
		)}),
    )

@admin.register(InscricaoAtividadeNoturna)
class InscricaoAtividadeNoturnaAdmin(admin.ModelAdmin):
    list_display = ['oficina', 'aluno']
    list_filter = ['oficina', 'aluno']
    autocomplete_fields = ['oficina', 'aluno']
    fieldsets = (
        (None, {'fields': (
			'oficina',
			'aluno'
		)}),
    )