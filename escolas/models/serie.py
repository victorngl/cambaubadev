from django.db import models
from .tipo_serie import TipoSerie
from .escola import Escola

class Serie(models.Model):
    """
       Classe Serie implementa as funções relacionadas a uma serie na plataforma.
    """

    nome = models.CharField(
        verbose_name="Série",
        max_length=200
    )

    tipo_serie = models.ForeignKey(
        TipoSerie,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Tipo da Série"
    )

    escola = models.ForeignKey(
        Escola,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Escola"
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
        return self.nome

    class META:
        app_label="escolas"
        verbose_name="Série"
        verbose_name_plural="Séries"
