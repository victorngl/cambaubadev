from django.db import models
from datetime import datetime
from django_quill.fields import QuillField
from .enquete import Enquete
from .resposta_enquete import RespostaEnquete
from crum import get_current_user

class Opcao(models.Model):
    """
       Classe Opcao implementa as funções relacionadas a uma opção na plataforma.
    """

    titulo = QuillField(
        verbose_name = "Título"
    )

    enquete = models.ForeignKey(
        Enquete,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Enquete"
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
    def quantidade_resposta_opcao(self):
        quantidade = RespostaEnquete.objects.filter(
            enquete=self.enquete,
            opcao=self.id
        ).count()
        
        return quantidade

    def __str__(self):
        return str(self.titulo)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Opcao, self).save(*args, **kwargs)
    
    class Meta:
        app_label = "enquetes"
        verbose_name = "Opção"
        verbose_name_plural = "Opções"