from django.db import models
from django.contrib.auth.models import Group
from datetime import datetime
from escolas.models import Escola
from crum import get_current_user

class DocumentacaoObra(models.Model):
    """
       Classe DocumentacaoObra implementa as funções relacionadas a uma documentação de obra na plataforma.
    """

    titulo = models.CharField(
		max_length=300,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

    data = models.DateField(
        verbose_name="Data",
        blank=True,
        null=True
    )

    descricao = models.TextField(
		verbose_name="Descrição",
		blank=True, null=True
	)
    
    anexo = models.FileField(
        verbose_name="Anexo",
        upload_to ='uploads/',
        blank=True
    )

    escola = models.ForeignKey(
        Escola,
        on_delete=models.SET_NULL,
        verbose_name='Escola',
        null=True
    )

    grupo_usuarios = models.ManyToManyField(
        Group,
        verbose_name='Grupo de Usuários',
        blank=True
    )

    foto = models.ImageField(
        verbose_name='Foto',  
        null=True, blank=True
    ) 

    foto_capa = models.ImageField(
        verbose_name='Foto de Capa',  
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

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(DocumentacaoObra, self).save(*args, **kwargs)

    class Meta:
        app_label = "informativos"
        verbose_name = "AEMC Notícia"
        verbose_name_plural = "AEMC Notícias"