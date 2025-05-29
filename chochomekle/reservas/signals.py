from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Cliente

# Signals para crear un cliente automáticamente cuando se crea un usuario
@receiver(post_save, sender=User)
def crear_cliente_automaticamente(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(
            usuario=instance,
            nombre=instance.username,  # o puedes personalizar esto
            telefono='',
            email=instance.email
        )

# Este codigo crea un cliente automáticamente cuando se crea un usuario.