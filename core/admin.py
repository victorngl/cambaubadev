from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from .models import Cidade, Endereco, Estado, Pais, Profile
from .forms import UserCreateForm

admin.site.unregister(User)


class ProfileAdminInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    extra = 1

@admin.register(User)
class UserAdmin(UserAdmin):
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

