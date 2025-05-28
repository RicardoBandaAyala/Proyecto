from django.shortcuts import render, get_object_or_404
from .models import Espacio, Reserva, Cliente
from .forms import ReservaForm
from django.http import HttpResponseRedirect
# Views para la aplicación de reservas

# View para la página de inicio que muestra los espacios disponibles

def inicio(request):
    espacios = Espacio.objects.all()
    return render(request, 'reservas/inicio.html', {'espacios': espacios})

# View para mostrar los detalles de un espacio específico
def detalle_espacio(request, id):
    espacio = get_object_or_404(Espacio, id=id)
    return render(request, 'reservas/detalle_espacio.html', {'espacio': espacio})

# View para crear una nueva reserva para un espacio específico
def crear_reserva(request, espacio_id):
    espacio = get_object_or_404(Espacio, id=espacio_id)
    # Si el método es POST, procesar el formulario de reserva
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.espacio = espacio
            reserva.save()
            return HttpResponseRedirect('/')
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'form': form, 'espacio': espacio})

# View para listar las reservas del usuario actual (o todas si no hay login)
def mis_reservas(request):
    reservas = Reserva.objects.all()  # Filtrar por usuario real si hay login
    return render(request, 'reservas/mis_reservas.html', {'reservas': reservas})

# View para el panel de administración que muestra todas las reservas
def panel_admin(request):
  
    reservas = Reserva.objects.all().order_by('cliente', 'fecha_inicio')                # Obtener todas las reservas y ordenarlas por cliente y fecha de inicio
    return render(request, 'reservas/panel_admin.html', {'reservas': reservas})
