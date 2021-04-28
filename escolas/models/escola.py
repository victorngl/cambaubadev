from django.db import models
from datetime import datetime

class Escola(models.Model):
    """
       Classe Escola implementa as funções relacionadas a uma escola na plataforma.
    """

    nome = models.CharField(
        verbose_name="Escola",
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

    class Meta:
        app_label="escolas"
        verbose_name="Escola"
        verbose_name_plural="Escolas"
