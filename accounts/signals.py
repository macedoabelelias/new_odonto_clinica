from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Paciente, Tratamento


@receiver(post_save, sender=Paciente)
def criar_tratamento_inicial(sender, instance, created, **kwargs):

    if created:

        Tratamento.objects.create(
            paciente=instance,
            titulo="Tratamento Inicial"
        )