from core.models.registro_interno import RegistroInterno
from core.models.pessoa import Pessoa
from core.models.dados_bancarios import DadosBancarios
from core.models.contato import Contato
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from .models import Cidade, Endereco, Estado, Pais, Profile
from .forms import UserCreateForm
from import_export import resources

admin.site.unregister(User)


class ProfileAdminInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    extra = 1

@admin.register(User)
class UserAdmin(UserAdmin, ImportExportModelAdmin):
    add_form = UserCreateForm
    inlines = [ProfileAdminInline]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'is_staff', 'password1', 'password2', 'groups' ),
        }),
    )


class EnderecoInline(admin.StackedInline):
    model = Endereco
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']
    fields = [
        'cep',
        'logradouro',
        'complemento',
        'numero',
        'bairro',
        'pais',
        'estado',
        'cidade',
    ]
    exclude = ['data_criacao']
    list_select_related = (
        'pais',
        'estado',
        'cidade',
    )
    extra=0

class CidadeAdmin(admin.StackedInline):
    model: Cidade
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

class ContatoAdmin(admin.StackedInline):
    model: Contato
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

class DadosBancariosAdmin(admin.StackedInline):
    model: DadosBancarios
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

class EstadoAdmin(admin.StackedInline):
    model: Estado
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

class PaisAdmin(admin.StackedInline):
    model: Pais
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

class PessoaAdmin(admin.StackedInline):
    model: Pessoa
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']

class RegistroInternoAdmin(admin.StackedInline):
    model: RegistroInterno
    readonly_fields = ['usuario_criacao', 'usuario_atualizacao']


