from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Classe Profile implementa as funções relacionadas a um profile na plataforma.
    """

    id_sigma = models.CharField(
        max_length=200,
        verbose_name="ID Sigma"
    )

    user = models.OneToOneField(
		User, 
		on_delete=models.CASCADE
	)

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name="Data de Atualização",
        auto_now=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "core"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

