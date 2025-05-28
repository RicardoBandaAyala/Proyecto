from django import forms
from .models import Reserva

# ReservaForm: Formulario para crear o editar reservas
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'fecha_inicio', 'fecha_fin']
