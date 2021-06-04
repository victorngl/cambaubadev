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
    ]

    autocomplete_fields = [
        'materia',
    ]

    def get_queryset(self, request):
        qs = super(AtividadeEscolarAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = super(AtividadeEscolarAdmin, self).get_queryset(request).filter(usuario_criacao=request.user)
            return qs
        return qs.filter(usuario_criacao=request.user)
