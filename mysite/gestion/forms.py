from django import forms
from .models import *

class EstiloFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class ClienteSoporteForm(EstiloFormMixin, forms.ModelForm):
    class Meta:
        model = ClienteSoporte
        fields = '__all__'
        widgets = {'fecha_registro': forms.DateInput(attrs={'type': 'date'})}

class AgenteSoporteForm(EstiloFormMixin, forms.ModelForm):
    class Meta:
        model = AgenteSoporte
        fields = '__all__'
        widgets = {'fecha_contratacion': forms.DateInput(attrs={'type': 'date'})}

class SLAForm(EstiloFormMixin, forms.ModelForm):
    class Meta:
        model = SLA
        fields = '__all__'

class BaseConocimientoForm(EstiloFormMixin, forms.ModelForm):
    class Meta:
        model = BaseConocimiento
        fields = '__all__'
        widgets = {'fecha_publicacion': forms.DateTimeInput(attrs={'type': 'datetime-local'})}

class TicketSoporteForm(EstiloFormMixin, forms.ModelForm):
    class Meta:
        model = TicketSoporte
        fields = '__all__'
        widgets = {
            'fecha_creacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_cierre': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class InteraccionForm(EstiloFormMixin, forms.ModelForm):
    class Meta:
        model = Interaccion
        fields = '__all__'
        widgets = {'fecha_interaccion': forms.DateTimeInput(attrs={'type': 'datetime-local'})}

class SatisfaccionClienteForm(EstiloFormMixin, forms.ModelForm):
    class Meta:
        model = SatisfaccionCliente
        fields = '__all__'
        widgets = {
            'fecha_encuesta': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_envio': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
