from atividades_escolares.models.atividade_escolar import AtividadeEscolar
from django.db import models
from crum import get_current_user

class AnexoAtividadeEscolar(models.Model):
    """
       Classe Anexo Atividade Escolar implementa as funções relacionadas aos anexos das atividades escolares.
    """

    titulo = models.CharField(
		max_length=250,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)
    
    anexo = models.FileField(
        verbose_name="Anexo",
        upload_to ='uploads/',
        blank=True
    )

    atividade_escolar = models.ForeignKey(
        AtividadeEscolar,
        verbose_name="Atividade Escolar",
        on_delete=models.SET_NULL,
        null=True
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
        return self.titulo + " " + self.anexo.name

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(AnexoAtividadeEscolar, self).save(*args, **kwargs)


    class Meta:
        app_label = "atividades_escolares"
        verbose_name = "Anexo"
        verbose_name_plural = "Anexos"
        ordering = ["-id"]