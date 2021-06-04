from django.db import models
from datetime import datetime
from colorfield.fields import ColorField
from crum import get_current_user

class Materia(models.Model):
    """
       Classe Materia implementa as funções relacionadas a uma materia na plataforma.
    """

    titulo = models.CharField(
        verbose_name="Título",
        max_length=200
    )

    hexadecimal = ColorField(
        default='#FF0000', 
        format='hexa'
    )

    data_alteracao = models.DateTimeField(
        verbose_name="Data de Alteração",
        auto_now=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    foto_capa = models.ImageField(
        verbose_name='Foto de Capa',  
        null=True, blank=True
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
        super(Materia, self).save(*args, **kwargs)

    class Meta:
        app_label="escolas"
        verbose_name="Matéria"
        verbose_name_plural="Matérias"
