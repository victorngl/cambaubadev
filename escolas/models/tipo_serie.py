from django.db import models
from datetime import datetime

class TipoSerie(models.Model):
    """
       Classe TipoSerie implementa as funções relacionadas a um tipo de série na plataforma.
    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=200
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
        verbose_name="Tipo de Série"
        verbose_name_plural="Tipos de série"
