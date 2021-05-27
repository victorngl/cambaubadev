from django.db import models
from crum import get_current_user
from django.contrib.auth.models import User


class Midia(models.Model):

    nome = models.CharField(
        max_length=30,
        verbose_name="Nome",
        help_text="Campo Obrigatório"
    )

    arquivo = models.FileField(
        verbose_name="Anexo",
        upload_to="midias/"
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    data_atualizacao = models.DateField(
        verbose_name="Data de Atualização",
        auto_now=True
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
        super(Midia, self).save(*args, **kwargs) 
    
    class Meta:
        app_label = "materiais_didaticos"
        verbose_name = "Mídia"
        verbose_name_plural = "Mídias"