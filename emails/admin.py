from django.contrib import admin
from .models.destinatario import Destinatario
from .models.template_email import TemplateEmail
from .models.mensagem_email import MensagemEmail



@admin.register(Destinatario)
class DestinatarioAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']


@admin.register(TemplateEmail)
class TemplateEmailAdmin(admin.ModelAdmin):
    list_display = ['assunto', 'codigo']
    search_fields = ['codigo']
    autocomplete_fields = ['destinatarios']
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']


@admin.register(MensagemEmail)
class MensagemEmailAdmin(admin.ModelAdmin):
    list_display = ['template_email', 'enviado', 'created_by']
    search_fields = ['email']
    autocomplete_fields = ['template_email', 'created_by']
    readonly_fields = ['template_email', 'enviado', 'created_by', 'usuario_atualizacao']
