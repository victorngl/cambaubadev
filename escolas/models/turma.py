from django.db import models
from datetime import datetime
from .serie import Serie
from .professor import Professor
from crum import get_current_user

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

    email_pai_responsavel = models.CharField(
        max_length=500,
        verbose_name="Email do Pai Responsável",
        null=True, blank=True
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

    @property
    def comunicados_exibicao(self):
        return self.comunicado_set.all()[:10]

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Turma, self).save(*args, **kwargs)


    class Meta:
        app_label="escolas"
        verbose_name="Turma"
        verbose_name_plural="Turmas"
