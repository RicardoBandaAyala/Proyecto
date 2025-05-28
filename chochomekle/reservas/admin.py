from django.contrib import admin
from .models import Cliente, Espacio, Reserva

# Registro de modelos en el panel de administración de Django
admin.site.register(Cliente)
#admin.site.register(Espacio)
admin.site.register(Reserva)

class EspacioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'capacidad')  # Opcional
    fields = ('nombre', 'ubicacion', 'capacidad', 'disponible', 'descripcion')  # 👈 Aquí defines qué mostrar

admin.site.register(Espacio, EspacioAdmin)