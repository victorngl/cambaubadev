from django.db import models
from crum import get_current_user

class TipoMaterialDidatico(models.Model):
    """
       Classe TipoMaterialDidatico implementa as funções relacionadas a um tipo de material didático na plataforma.
    """

    tipo = models.CharField(
		verbose_name="Tipo",
        max_length=250,
		help_text="Campo Obrigatório*"
	)
    icone = models.ImageField(
        verbose_name="Ícone",
        upload_to="tipos_arquivo/"
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
        return self.tipo

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(TipoMaterialDidatico, self).save(*args, **kwargs) 
    
    class Meta:
        app_label = "materiais_didaticos"
        verbose_name = "Tipo de Material Didático"
        verbose_name_plural = "Tipos de Materiais Didáticos"