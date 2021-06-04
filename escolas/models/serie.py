from django.db import models
from datetime import datetime
from .tipo_serie import TipoSerie
from .escola import Escola
from crum import get_current_user

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
        return self.nome

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Serie, self).save(*args, **kwargs)

    class Meta:
        app_label="escolas"
        verbose_name="Série"
        verbose_name_plural="Séries"
