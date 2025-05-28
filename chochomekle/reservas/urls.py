# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('espacio/<int:id>/', views.detalle_espacio, name='detalle_espacio'),
    path('crear/', views.crear_reserva, name='crear_reserva'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('admin-panel/', views.panel_admin, name='panel_admin'),
    path('detalle_espacio/', views.detalle_espacio, name='detalle_espacio'),
]
# Este archivo define las rutas de la aplicación de reservas, incluyendo la página de inicio, creación de reservas, gestión de reservas del usuario, panel de administración y autenticación.