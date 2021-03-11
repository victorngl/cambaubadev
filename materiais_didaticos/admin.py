from django.contrib import admin
from .models import AtaReuniao, CalendarioAtividade, Comunicado, MaterialDidatico


@admin.register(AtaReuniao)
class AtaReuniaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data']

@admin.register(CalendarioAtividade)
class CalendarioAtividadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_inicial', 'data_final']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data_inicial', 'data_final']

@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data']

@admin.register(MaterialDidatico)
class MaterialDidaticoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo']
    filter_horizontal = ['turmas']
    search_fields = ['titulo']