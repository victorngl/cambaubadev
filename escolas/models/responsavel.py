from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, Group
from core.models import Pessoa
from crum import get_current_user

class Responsavel(Pessoa):
    """
       Classe Professor implementa as funções relacionadas a um professor na plataforma.
    """
    id_acesso = models.CharField(
        max_length=200,
        verbose_name="ID Acesso",
        blank=True, null=True
    )

    id_sigma = models.CharField(
        max_length=200,
        verbose_name="ID Sigma",
        blank=True, null=True
    )

    username = models.CharField(
        max_length=200,
        verbose_name="Usuário",
        blank=True, null=True
    )

    senha = models.CharField(
        max_length=200,
        verbose_name="Senha",
        blank=True, null=True
    )

    usuario = models.ForeignKey(
        User,
        verbose_name="Usuário do Professor",
        on_delete=models.SET_NULL,
        related_name='usuario_responsavel',
        unique=True,
        blank=True,
        null=True
    )

    def sincronizar_responsavel(self):
        from core.models import Profile
        print("Sincronizando")
        if self.username and not self.usuario:
            novo_usuario = User.objects.create(
                username=self.username
            )
            novo_usuario.set_password(self.senha)
            novo_usuario.save()

            grupo_professor = Group.objects.get(name='Responsavel') 
            grupo_professor.user_set.add(novo_usuario)

            self.usuario = novo_usuario
            self.save()

            novo_profile = Profile.objects.create(
                user=novo_usuario,
                id_sigma=self.id_sigma
            )

    def __str__(self):
        return self.nome

    class Meta:
        app_label="escolas"
        verbose_name="Responsável"
        verbose_name_plural="Responsáveis"
