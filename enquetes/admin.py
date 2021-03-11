from django.contrib import admin
from .models import Enquete, RespostaEnquete


@admin.register(Enquete)
class EnqueteAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_expiracao']
    search_fields = ['titulo']
    filter_horizontal = ['grupo_usuarios']
    fieldsets = (
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
			'anexo'
		)}),
        ('Opções da enquete', {'fields': (
			'opcao_1',
			'opcao_2',
			'opcao_3',
			'opcao_4',
		)}),
        ('Configurações', {'fields': (
			'mostrar_resultado',
			'grupo_usuarios'
		)})
    )

@admin.register(RespostaEnquete)
class RespostaEnqueteAdmin(admin.ModelAdmin):
    list_display = ['id', 'opcao', 'enquete', 'usuario_inscricao']
    autocomplete_fields = ['enquete', 'usuario_inscricao']
    list_filter = ['enquete']
    search_fields = ['opcao']
    fieldsets = (
        (None, {'fields': (
			'enquete',
			'opcao'
		)}),
    )