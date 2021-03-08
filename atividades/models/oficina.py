from django.db import models
from datetime import datetime
from escolas.models import Turma

class Oficina(models.Model):
    """
       Classe Oficina implementa as funções relacionadas a uma oficina na plataforma.
    """

    titulo = models.CharField(
		max_length=250,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

    vagas = models.IntegerField(
		verbose_name="Vagas",
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

    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True, null=True
    )

    turmas = models.ManyToManyField(
        Turma,
        verbose_name=("Turmas"),
        blank=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "atividades"
        verbose_name = "Oficina"
        verbose_name_plural = "Oficinas"