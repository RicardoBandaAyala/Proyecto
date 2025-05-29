from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Espacio, Reserva, Cliente
from .forms import ReservaForm, BuscarEspacioForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from datetime import date
from django.contrib import messages
# Views para la aplicación de reservas

# View para la página de inicio que muestra los espacios disponibles
def inicio(request):
    espacios = Espacio.objects.all()
    q = request.GET.get('q')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    mensaje = ""
    form = BuscarEspacioForm(request.GET or None)

    # Filtrar espacios por fecha si se proporcionan
    if q:
        espacios = espacios.filter(nombre__icontains=q)

    # Filtrar espacios por nombre y fechas de inicio y fin
    if fecha_inicio and fecha_fin:
        reservas_ocupadas = Reserva.objects.filter(
            Q(fecha_inicio__lte=fecha_fin), Q(fecha_fin__gte=fecha_inicio)
        ).values_list('espacio_id', flat=True)

        espacios = espacios.exclude(id__in=reservas_ocupadas)

    context = {
        'espacios': espacios,
        'q': q,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'espacios': espacios,
        'form': form,
        'mensaje': mensaje
    }
    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")
        fecha_inicio = form.cleaned_data.get("fecha_inicio")
        fecha_fin = form.cleaned_data.get("fecha_fin")

        if nombre:
            espacios = espacios.filter(nombre__icontains=nombre)

            if not espacios.exists():
                mensaje = "No hay espacios disponibles para esas fechas."

    
    return render(request, "reservas/inicio.html", context)

# View para mostrar los detalles de un espacio específico
def detalle_espacio(request, id):
    espacio = get_object_or_404(Espacio, id=id)
    return render(request, 'reservas/detalle_espacio.html', {'espacio': espacio})

# View para crear una nueva reserva para un espacio específico
def crear_reserva(request, espacio_id):
    espacio = get_object_or_404(Espacio, id=espacio_id)

    # Buscar o crear automáticamente el Cliente
    cliente, created = Cliente.objects.get_or_create(
        nombre=request.user.username  # o ajusta según tu modelo
    )

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.cliente = cliente
            reserva.espacio = espacio
            reserva.save()
            return redirect('mis_reservas')
    else:
        form = ReservaForm()

    return render(request, 'reservas/crear_reserva.html', {
        'form': form,
        'espacio': espacio
    })

# View para listar las reservas del usuario actual (o todas si no hay login)
def mis_reservas(request):
    try:
        cliente = Cliente.objects.get(nombre=request.user)  # Obtener el perfil del cliente asociado al usuario actual
        reservas = Reserva.objects.filter(cliente=cliente).select_related('espacio')
    except Cliente.DoesNotExist:
        reservas = []  # El usuario aún no tiene un perfil de Cliente
    return render(request, 'reservas/mis_reservas.html', {'reservas': reservas})

# View para actualizar una reserva existente
@login_required
def actualizar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, cliente=request.user)

    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in ['pendiente', 'confirmada', 'cancelada']:
            reserva.estado = nuevo_estado
            reserva.save()
            messages.success(request, 'Estado actualizado correctamente.')
        else:
            messages.error(request, 'Estado inválido.')
    return redirect('mis_reservas')

# View para el panel de administración que muestra todas las reservas
def panel_admin(request):
  
    reservas = Reserva.objects.all().order_by('cliente', 'fecha_inicio')                # Obtener todas las reservas y ordenarlas por cliente y fecha de inicio
    return render(request, 'reservas/panel_admin.html', {'reservas': reservas})
