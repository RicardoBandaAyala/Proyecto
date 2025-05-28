from django.urls import path
from . import views

# URLs para la aplicación de reservas
# Este archivo define las rutas de la aplicación de reservas
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('espacio/<int:espacio_id>/', views.detalle_espacio, name='detalle_espacio'),
    path('reservar/<int:espacio_id>/', views.crear_reserva, name='crear_reserva'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('admin-panel/', views.panel_admin, name='panel_admin'),
]
