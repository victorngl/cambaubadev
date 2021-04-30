from django.db import models
from datetime import datetime
from .serie import Serie
from .professor import Professor

class Turma(models.Model):
    """
       Classe Turma implementa as funções relacionadas a uma turma na plataforma.
    """

    nome = models.CharField(
        verbose_name="Título",
        max_length=200
    )

    serie = models.ForeignKey(
        Serie,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Série"
    )

    professores = models.ManyToManyField(
        Professor,
        verbose_name=("Professor"),
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

    @property
    def comunicados_exibicao(self):
        return self.comunicado_set.all()[:10]

    def __str__(self):
        return self.nome

    class Meta:
        app_label="escolas"
        verbose_name="Turma"
        verbose_name_plural="Turmas"
