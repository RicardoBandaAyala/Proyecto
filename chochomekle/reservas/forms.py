from django import forms
from .models import Reserva

# Formulario para crear o editar reservas
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            # Define los widgets para los campos del formulario
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'espacio': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
# Formulario para buscar espacios disponibles
class BuscarEspacioForm(forms.Form):
    nombre = forms.CharField(required=False, label="¿Adónde vas?")
    fecha_inicio = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))


