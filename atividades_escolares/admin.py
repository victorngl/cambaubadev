from atividades_escolares.models.anexos_atividade_escolar import AnexosAtividadeEscolar
from django.contrib import admin
from .models import AtividadeEscolar


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
        'anexos'
    ]

    autocomplete_fields = [
        'materia',    
    ]

    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

    def get_queryset(self, request):
        queryset = super(AtividadeEscolarAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            queryset = super(AtividadeEscolarAdmin, self).get_queryset(request).filter(usuario_criacao=request.user)
            return queryset
        return queryset


@admin.register(AnexosAtividadeEscolar)
class AnexosAtividadeEscolarAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo']
    search_fields = ['titulo']
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']