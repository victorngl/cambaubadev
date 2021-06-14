from django.contrib import admin
from .models import Balancete, BalancoPatrimonial, DocumentacaoObra, AtaReuniao

@admin.register(Balancete)
class BalanceteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
        'data',
        'escola',
    ]

    list_filter = [
        'escola',
    ]

    autocomplete_fields = [
        'escola',
    ]

    search_fields = [
        'titulo',
    ]
    
    filter_horizontal = [
        'grupo_usuarios',
    ]

    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

@admin.register(BalancoPatrimonial)
class BalancoPatrimonialAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
        'data',
        'escola',
    ]

    list_filter = [
        'escola',
    ]

    autocomplete_fields = [
        'escola',
    ]

    search_fields = [
        'titulo',
    ]
    
    filter_horizontal = [
        'grupo_usuarios',
    ]

    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

@admin.register(DocumentacaoObra)
class DocumentacaoObraAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
        'data',
        'escola',
    ]

    list_filter = [
        'escola',
    ]

    autocomplete_fields = [
        'escola',
    ]

    search_fields = [
        'titulo',
    ]
    
    filter_horizontal = [
        'grupo_usuarios',
    ]

    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

# @admin.register(AtaReuniao)
# class AtaReuniaoAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'titulo',
#         'data',
#     ]

#     search_fields = [
#         'titulo',
#         'data',
#     ]
    
#     filter_horizontal = [
#         'turmas',
#     ]

#     readonly_fields = ['usuario_criacao', 'usuario_atualizacao']