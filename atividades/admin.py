from django.contrib import admin
from .models import Oficina, AtividadeExtra, AtividadeNoturna, InscricaoOficina, InscricaoAtividadeExtra, InscricaoAtividadeNoturna

admin.site.register(AtividadeExtra)
admin.site.register(AtividadeNoturna)
admin.site.register(InscricaoOficina)
admin.site.register(InscricaoAtividadeExtra)
admin.site.register(InscricaoAtividadeNoturna)


@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'vagas', 'data_inicial', 'data_final']
    filter_horizontal = ['turmas']