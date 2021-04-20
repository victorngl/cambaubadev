from django.contrib import admin
from django.conf import settings
from .models import Enquete, RespostaEnquete, Opcao

class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 1


@admin.register(Enquete)
class EnqueteAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_expiracao']
    search_fields = ['titulo']
    filter_horizontal = ['grupo_usuarios']
    fieldsets = (
        ('Dados Principais', {'fields': [
			'titulo',
			'descricao',
            'data_expiracao',
			'anexo',
        ]}),
        ('Configurações', {'fields': [
            'voto_unico',
			'mostrar_resultado',
			'grupo_usuarios',
            'retrato',
            'foto_capa',
        ]}),
    )
    change_form_template = "admin/enquete_change_form.html"
    inlines = [OpcaoInline]



@admin.register(RespostaEnquete)
class RespostaEnqueteAdmin(admin.ModelAdmin):
    list_display = ['id', 'enquete', 'usuario_votante']
    autocomplete_fields = ['enquete', 'usuario_votante']
    list_filter = ['enquete']
    fieldsets = (
        (None, {'fields': [
			'enquete',
            'opcao',
            'usuario_votante'
        ]}),
    )

@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'enquete']
    autocomplete_fields = ['enquete']
    list_filter = ['enquete']
    fieldsets = (
        ('Opções', {'fields': [
			'titulo',
        ]}),
    )