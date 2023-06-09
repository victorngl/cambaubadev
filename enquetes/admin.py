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
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']
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
            'foto',
            'foto_capa',
        ]}),
    )
    change_form_template = "admin/enquete_change_form.html"
    inlines = [OpcaoInline]



@admin.register(RespostaEnquete)
class RespostaEnqueteAdmin(admin.ModelAdmin):
    list_display = ['id', 'enquete', 'usuario_votante']
    autocomplete_fields = ['enquete', 'usuario_votante']
    readonly_fields = ['usuario_votante', 'usuario_atualizacao', 'opcao_escolha']
    list_filter = ['enquete']
    fieldsets = (
        (None, {'fields': [
			'enquete',
            'usuario_votante',
            'opcao_escolha',
        ]}),
    )

@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'enquete']
    autocomplete_fields = ['enquete']
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']
    list_filter = ['enquete']
    fieldsets = (
        ('Opções', {'fields': [
			'titulo',
        ]}),
    )