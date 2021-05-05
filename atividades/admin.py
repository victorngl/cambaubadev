from django.contrib import admin
from .models import Oficina, AtividadeExtra, AtividadeNoturna, InscricaoOficina, Olimpiada, InscricaoAtividadeExtra, InscricaoAtividadeNoturna

class InscricaoOficinaInline(admin.TabularInline):
    model = InscricaoOficina
    fields = ['aluno', 'usuario_inscricao', 'data_criacao']
    readonly_fields = ['aluno', 'usuario_inscricao', 'data_criacao']
    can_delete = False
    extra = 0

class InscricaoAtividadeExtraInline(admin.TabularInline):
    model = InscricaoAtividadeExtra
    fields = ['aluno', 'usuario_inscricao', 'data_criacao']
    readonly_fields = ['aluno', 'usuario_inscricao', 'data_criacao']
    can_delete = False
    extra = 0

class InscricaoAtividadeNoturnaInline(admin.TabularInline):
    model = InscricaoAtividadeNoturna
    fields = ['aluno', 'usuario_inscricao', 'data_criacao']
    readonly_fields = ['aluno', 'usuario_inscricao', 'data_criacao']
    can_delete = False
    extra = 0

@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'vagas', 'quantidade_inscritos', 'horario', 'data_inicial', 'data_final']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data_inicial', 'data_final']
    inlines = [InscricaoOficinaInline] 

@admin.register(AtividadeExtra)
class AtividadeExtraAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'vagas', 'quantidade_inscritos', 'horario', 'data_inicial', 'data_final']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data_inicial', 'data_final']
    inlines = [InscricaoAtividadeExtraInline]

@admin.register(AtividadeNoturna)
class AtividadeNoturnaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'vagas', 'quantidade_inscritos', 'horario', 'data_inicial', 'data_final']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data_inicial', 'data_final']
    inlines = [InscricaoAtividadeNoturnaInline]

@admin.register(Olimpiada)
class OlimpiadaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_inicial', 'data_final']
    search_fields = ['titulo', 'data_inicial', 'data_final']

@admin.register(InscricaoOficina)
class InscricaoOficinaAdmin(admin.ModelAdmin):
    list_display = ['oficina', 'aluno', 'usuario_inscricao', 'data_criacao']
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
    list_display = ['atividade_extra', 'aluno', 'data_criacao']
    list_filter = ['atividade_extra', 'aluno']
    autocomplete_fields = ['atividade_extra', 'aluno']
    fieldsets = (
        (None, {'fields': (
            'atividade_extra',
            'aluno'
        )}),
    )

@admin.register(InscricaoAtividadeNoturna)
class InscricaoAtividadeNoturnaAdmin(admin.ModelAdmin):
    list_display = ['atividade_noturna', 'aluno', 'data_criacao']
    list_filter = ['atividade_noturna', 'aluno']
    autocomplete_fields = ['atividade_noturna', 'aluno']
    fieldsets = (
        (None, {'fields': (
            'atividade_noturna',
            'aluno'
        )}),
    )
