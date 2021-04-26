from django.contrib import admin
from .models import CalendarioAtividade, Comunicado, MaterialDidatico, TipoMaterialDidatico

@admin.register(CalendarioAtividade)
class CalendarioAtividadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_inicial', 'data_final']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data_inicial', 'data_final']
    autocomplete_fields = ['materia']

@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data']
    filter_horizontal = ['turmas']
    exclude = ['usuario_criacao']
    search_fields = ['titulo', 'data']

@admin.register(MaterialDidatico)
class MaterialDidaticoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'tipo', 'materia']
    autocomplete_fields = ['tipo', 'materia']

@admin.register(TipoMaterialDidatico)
class TipoMaterialDidaticoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo']
    search_fields = ['tipo']
