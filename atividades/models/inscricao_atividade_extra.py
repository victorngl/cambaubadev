from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .oficina import Oficina
from escolas.models import Aluno

class InscricaoAtividadeExtra(models.Model):
    """
       Classe InscricaoAtividadeExtra implementa as funções relacionadas a inscrição de uma atividade extra na plataforma.
    """

    oficina = models.ForeignKey(
		Oficina,
        on_delete=models.SET_NULL,
        null=True,
		verbose_name="Oficina"
	)

    aluno = models.ForeignKey(
		Aluno,
        on_delete=models.SET_NULL,
        null=True,
		verbose_name="Aluno"
	)

    usuario_inscricao = models.ForeignKey(
		User,
        on_delete=models.SET_NULL,
        null=True,
		verbose_name="Usuário Inscrição"
	)

    data_alteracao = models.DateTimeField(
        verbose_name="Data de Alteração",
        auto_now=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = "atividades"
        verbose_name = "Inscrição na Atividade Extra"
        verbose_name_plural = "Inscrições na Atividade Extra"