from django.contrib import admin
from .models import Cliente, Espacio, Reserva

# Registro de modelos en el panel de administración de Django
admin.site.register(Cliente)
admin.site.register(Espacio)
admin.site.register(Reserva)
