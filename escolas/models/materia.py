from django.db import models
from datetime import datetime

class Materia(models.Model):
    """
       Classe Materia implementa as funções relacionadas a uma materia na plataforma.
    """

    titulo = models.CharField(
        verbose_name="Título",
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
        return self.titulo

    class META:
        app_label="escolas"
        verbose_name="Matéria"
        verbose_name_plural="Matérias"
