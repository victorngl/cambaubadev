from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from core.models import Pessoa

class Professor(Pessoa):
    """
       Classe Professor implementa as funções relacionadas a um professor na plataforma.
    """

    usuario = models.ForeignKey(
        User,
        verbose_name="Usuário do Professor",
        related_name="usuario_professor",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome

    class META:
        app_label="escolas"
        verbose_name="Professor"
        verbose_name_plural="Professores"
