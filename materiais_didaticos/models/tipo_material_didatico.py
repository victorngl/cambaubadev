from django.db import models
from datetime import datetime

class TipoMaterialDidatico(models.Model):
    """
       Classe TipoMaterialDidatico implementa as funções relacionadas a um tipo de material didático na plataforma.
    """

    titulo = models.CharField(
		max_length=250,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

    data_alteracao = models.DateTimeField(
        verbose_name="Data de Alteração",
        auto_now=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo
        
    class Meta:
        app_label = "tipos_materiais_didaticos"
        verbose_name = "Tipo de Material Didático"
        verbose_name_plural = "Tipos de Materiais Didáticos"