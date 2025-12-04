from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import *
from .forms import *

class HomeView(TemplateView):
    template_name = 'gestion/index.html'

# --- CLIENTES ---
class ClienteListView(ListView):
    model = ClienteSoporte
    template_name = 'gestion/cliente_list.html'

class ClienteCreateView(CreateView):
    model = ClienteSoporte
    form_class = ClienteSoporteForm
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = ClienteSoporte
    form_class = ClienteSoporteForm
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = ClienteSoporte
    template_name = 'gestion/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

# --- AGENTES ---
class AgenteListView(ListView):
    model = AgenteSoporte
    template_name = 'gestion/agente_list.html'

class AgenteCreateView(CreateView):
    model = AgenteSoporte
    form_class = AgenteSoporteForm
    template_name = 'gestion/agente_form.html'
    success_url = reverse_lazy('agente_list')

class AgenteUpdateView(UpdateView):
    model = AgenteSoporte
    form_class = AgenteSoporteForm
    template_name = 'gestion/agente_form.html'
    success_url = reverse_lazy('agente_list')

class AgenteDeleteView(DeleteView):
    model = AgenteSoporte
    template_name = 'gestion/agente_confirm_delete.html'
    success_url = reverse_lazy('agente_list')

# --- SLA ---
class SLAListView(ListView):
    model = SLA
    template_name = 'gestion/sla_list.html'

class SLACreateView(CreateView):
    model = SLA
    form_class = SLAForm
    template_name = 'gestion/sla_form.html'
    success_url = reverse_lazy('sla_list')

class SLAUpdateView(UpdateView):
    model = SLA
    form_class = SLAForm
    template_name = 'gestion/sla_form.html'
    success_url = reverse_lazy('sla_list')

class SLADeleteView(DeleteView):
    model = SLA
    template_name = 'gestion/sla_confirm_delete.html'
    success_url = reverse_lazy('sla_list')

# --- TICKETS ---
class TicketListView(ListView):
    model = TicketSoporte
    template_name = 'gestion/ticket_list.html'

class TicketCreateView(CreateView):
    model = TicketSoporte
    form_class = TicketSoporteForm
    template_name = 'gestion/ticket_form.html'
    success_url = reverse_lazy('ticket_list')

class TicketUpdateView(UpdateView):
    model = TicketSoporte
    form_class = TicketSoporteForm
    template_name = 'gestion/ticket_form.html'
    success_url = reverse_lazy('ticket_list')

class TicketDeleteView(DeleteView):
    model = TicketSoporte
    template_name = 'gestion/ticket_confirm_delete.html'
    success_url = reverse_lazy('ticket_list')

# --- INTERACCIONES ---
class InteraccionListView(ListView):
    model = Interaccion
    template_name = 'gestion/interaccion_list.html'

class InteraccionCreateView(CreateView):
    model = Interaccion
    form_class = InteraccionForm
    template_name = 'gestion/interaccion_form.html'
    success_url = reverse_lazy('interaccion_list')

class InteraccionUpdateView(UpdateView):
    model = Interaccion
    form_class = InteraccionForm
    template_name = 'gestion/interaccion_form.html'
    success_url = reverse_lazy('interaccion_list')

class InteraccionDeleteView(DeleteView):
    model = Interaccion
    template_name = 'gestion/interaccion_confirm_delete.html'
    success_url = reverse_lazy('interaccion_list')

# --- BASE CONOCIMIENTO ---
class BaseConocimientoListView(ListView):
    model = BaseConocimiento
    template_name = 'gestion/base_conocimiento_list.html'

class BaseConocimientoCreateView(CreateView):
    model = BaseConocimiento
    form_class = BaseConocimientoForm
    template_name = 'gestion/base_conocimiento_form.html'
    success_url = reverse_lazy('base_conocimiento_list')

class BaseConocimientoUpdateView(UpdateView):
    model = BaseConocimiento
    form_class = BaseConocimientoForm
    template_name = 'gestion/base_conocimiento_form.html'
    success_url = reverse_lazy('base_conocimiento_list')

class BaseConocimientoDeleteView(DeleteView):
    model = BaseConocimiento
    template_name = 'gestion/base_conocimiento_confirm_delete.html'
    success_url = reverse_lazy('base_conocimiento_list')

# --- SATISFACCION ---
class SatisfaccionListView(ListView):
    model = SatisfaccionCliente
    template_name = 'gestion/satisfaccion_cliente_list.html'

class SatisfaccionCreateView(CreateView):
    model = SatisfaccionCliente
    form_class = SatisfaccionClienteForm
    template_name = 'gestion/satisfaccion_cliente_form.html'
    success_url = reverse_lazy('satisfaccion_cliente_list')

class SatisfaccionUpdateView(UpdateView):
    model = SatisfaccionCliente
    form_class = SatisfaccionClienteForm
    template_name = 'gestion/satisfaccion_cliente_form.html'
    success_url = reverse_lazy('satisfaccion_cliente_list')

class SatisfaccionDeleteView(DeleteView):
    model = SatisfaccionCliente
    template_name = 'gestion/satisfaccion_cliente_confirm_delete.html'
    success_url = reverse_lazy('satisfaccion_cliente_list')