from django.contrib import admin
from .models import Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data', 'hora_inicio', 'hora_termino']