from django.db import models
# Crear modelos para la aplicación de reservas

# Cliente: Representa a un cliente que realiza reservas
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# Espacio: Representa un espacio que se puede reservar
class Espacio(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
# Reserva: Representa una reserva realizada por un cliente para un espacio
class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"{self.cliente} - {self.espacio} ({self.fecha_inicio})"
    
    # Meta: Configuración adicional del modelo Reserva que define el orden por fecha de inicio
    class Meta:
        ordering = ['fecha_inicio']
# Quitar el siguiente comentario de superusuario (solo para pruebas)
# SuperUser: Chochomekle
# Contraseña: contraseña123