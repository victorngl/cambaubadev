from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data', 'hora_inicio', 'hora_termino']
    readonly_fields = ['data_criacao','usuario_criacao', 'usuario_atualizacao']