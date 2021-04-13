from django.contrib import admin
from .models import Enquete, RespostaEnquete, Opcao

class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 5


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
        ]}),('Configurações', {'fields': [
            'voto_unico',
			'mostrar_resultado',
			'grupo_usuarios',
        ]}),
    )
    inlines = [OpcaoInline]



@admin.register(RespostaEnquete)
class RespostaEnqueteAdmin(admin.ModelAdmin):
    list_display = ['id', 'enquete', 'usuario_votante']
    autocomplete_fields = ['enquete', 'usuario_votante']
    list_filter = ['enquete']
    fieldsets = (
        (None, {'fields': [
			'enquete'
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