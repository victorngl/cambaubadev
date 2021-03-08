from django.db import models
from datetime import datetime
from escolas.models import Turma

class CalendarioAtividade(models.Model):
    """
       Classe CalendarioAtividade implementa as funções relacionadas a um calendário de atividade na plataforma.
    """

    titulo = models.CharField(
		max_length=250,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True, null=True
    )

    data_inicial = models.DateField(
        verbose_name="Data Inicial",
		blank=True, null=True
    )

    data_final = models.DateField(
        verbose_name="Data Final",
		blank=True, null=True
    )

    turmas = models.ManyToManyField(
        Turma,
        verbose_name=("Turmas"),
        blank=True
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
        return self.titulo

    class Meta:
        app_label = "materiais_didaticos"
        verbose_name = "Calendário de Atividade"
        verbose_name_plural = "Calendário de Atividades"