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
