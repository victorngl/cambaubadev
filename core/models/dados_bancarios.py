
from django.db import models


class DadosBancarios(models.Model):
    """
       Classe Dados Bancorios implementa as funções relacionadas a um dado bancario na plataforma.
    """

    banco = models.CharField(
        verbose_name="Banco",
        max_length=200
    )

    agencia = models.CharField(
        verbose_name="Agencia",
        max_length=200
    )

    operacao = models.IntegerField(
        verbose_name="Operacao"
    )

    numero_conta = models.CharField(
        verbose_name="Numero da conta",
        max_length=200
    )

    def __str__(self):
        return self.banco


    class META:
        app_label="core"
        verbose_name="Dado Bancario"
        verbose_name_plural="Dados Bancarios"





