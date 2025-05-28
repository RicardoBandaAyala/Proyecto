from django.urls import path
from . import api_views

urlpatterns = [
    path('espacios/', api_views.EspacioList.as_view()),
    path('reservas/', api_views.ReservaList.as_view()),
    path('reservas/nueva/', api_views.CrearReserva.as_view()),
    path('clientes/<int:pk>/', api_views.ClienteDetail.as_view()),
    path('reservas/<int:pk>/actualizar/', api_views.ActualizarEstadoReserva.as_view()),
]
# Este archivo define las rutas de la API de reservas que permite gestionar reservas, espacios y clientes.