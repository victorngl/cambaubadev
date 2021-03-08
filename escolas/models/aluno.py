from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from core.models import Pessoa
from .turma import Turma

class Aluno(Pessoa):
    """
       Classe Aluno implementa as funções relacionadas a um aluno na plataforma.
    """

    pai = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='pai_aluno',
        null=True,
        verbose_name="Pai"
    )

    mae = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='mae_aluno',
        null=True,
        verbose_name="Mãe"
    )

    turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Turma"
    )

    observacao = models.TextField(
		verbose_name="Observação",
		blank=True, null=True
	)

    def __str__(self):
        return self.nome

    class META:
        app_label="escolas"
        verbose_name="Aluno"
        verbose_name_plural="Alunos"
