from django.db import models

class TipoMaterialDidatico(models.Model):
    """
       Classe TipoMaterialDidatico implementa as funções relacionadas a um tipo de material didático na plataforma.
    """

    tipo = models.CharField(
		verbose_name="Tipo",
        max_length=250,
		help_text="Campo Obrigatório*"
	)

    def __str__(self):
        return self.tipo
    
    class Meta:
        app_label = "materiais_didaticos"
        verbose_name = "Tipo de Material Didático"
        verbose_name_plural = "Tipos de Materiais Didáticos"