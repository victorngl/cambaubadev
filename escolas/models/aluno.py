from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from core.models import Pessoa
from .turma import Turma

class Aluno(Pessoa):
    """
       Classe Aluno implementa as funções relacionadas a um aluno na plataforma.
    """

    qtd_atividades_permitidas = models.IntegerField(
		verbose_name="Quantidade de Atividades Permitidas",
        default=1,
		blank=True, null=True
	)

    turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Turma"
    )

    usuario = models.ForeignKey(
        User,
        verbose_name="Usuário do Aluno",
        related_name="usuario_aluno",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    responsavel1 = models.ForeignKey(
        User,
        verbose_name="Responsável 1",
        related_name="responsavel1_aluno",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    responsavel2 = models.ForeignKey(
        User,
        verbose_name="Responsável 2",
        related_name="responsavel2_aluno",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    responsavel3 = models.ForeignKey(
        User,
        verbose_name="Responsável 3",
        related_name="responsavel3_aluno",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
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
