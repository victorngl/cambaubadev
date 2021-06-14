from atividades_escolares.models.anexo_atividade_escolar import AnexoAtividadeEscolar
from django.contrib import admin
from .models import AtividadeEscolar
from atividades_escolares import models

class AnexoAtividadeEscolarInline(admin.TabularInline):
    model = AnexoAtividadeEscolar
    extra = 0 
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

@admin.register(AtividadeEscolar)
class AtividadeEscolarAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
        'data_inicial',
        'data_final',
    ]
    
    search_fields = [
        'titulo',
        'data_inicial',
        'data_final',
    ]

    filter_horizontal = [
        'turmas',
    ]

    autocomplete_fields = [
        'materia',    
    ]

    inlines =[
        AnexoAtividadeEscolarInline
    ]

    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

    def get_queryset(self, request):
        queryset = super(AtividadeEscolarAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            queryset = super(AtividadeEscolarAdmin, self).get_queryset(request).filter(usuario_criacao=request.user)
            return queryset
        return queryset
