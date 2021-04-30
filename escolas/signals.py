from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Professor, Responsavel


@receiver(post_save, sender=Professor)
def sincronizar_professor(sender, instance, **kwargs):
    instance.sincronizar_professor()

@receiver(post_save, sender=Responsavel)
def sincronizar_responsavel(sender, instance, **kwargs):
    instance.sincronizar_responsavel()