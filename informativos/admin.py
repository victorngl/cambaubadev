from django.contrib import admin
from .models import Balancete, BalancoPatrimonial, DocumentacaoObra, AtaReuniao

@admin.register(Balancete)
class BalanceteAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data', 'escola']
    list_filter = ['escola']
    autocomplete_fields = ['escola']
    search_fields = ['titulo']

@admin.register(BalancoPatrimonial)
class BalancoPatrimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data', 'escola']
    list_filter = ['escola']
    autocomplete_fields = ['escola']
    search_fields = ['titulo']

@admin.register(DocumentacaoObra)
class DocumentacaoObraAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data', 'escola']
    list_filter = ['escola']
    autocomplete_fields = ['escola']
    search_fields = ['titulo']

@admin.register(AtaReuniao)
class AtaReuniaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data']
    filter_horizontal = ['turmas']
    search_fields = ['titulo', 'data']