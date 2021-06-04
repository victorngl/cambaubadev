
from django.db import models
from crum import get_current_user


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

    usuario_criacao = models.ForeignKey(
		'auth.User', 
		related_name='%(class)s_requests_created',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    usuario_atualizacao = models.ForeignKey(
		'auth.User', 
		related_name='%(class)s_requests_modified',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    def __str__(self):
        return self.banco

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(DadosBancarios, self).save(*args, **kwargs)

    class META:
        app_label="core"
        verbose_name="Dado Bancario"
        verbose_name_plural="Dados Bancarios"





