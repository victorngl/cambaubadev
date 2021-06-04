from django.db import models
from datetime import datetime
from crum import get_current_user

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
        super(Escola, self).save(*args, **kwargs)

    class Meta:
        app_label="escolas"
        verbose_name="Escola"
        verbose_name_plural="Escolas"
