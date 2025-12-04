from django.urls import path
from .views import (
    HomeView,
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    AgenteListView,
    AgenteCreateView,
    AgenteUpdateView,
    AgenteDeleteView,
    SLAListView,
    SLACreateView,
    SLAUpdateView,
    SLADeleteView,
    TicketListView,
    TicketCreateView,
    TicketUpdateView,
    TicketDeleteView,
    InteraccionListView,
    InteraccionCreateView,
    InteraccionUpdateView,
    InteraccionDeleteView,
    BaseConocimientoListView,
    BaseConocimientoCreateView,
    BaseConocimientoUpdateView,
    BaseConocimientoDeleteView,
    SatisfaccionListView,
    SatisfaccionCreateView,
    SatisfaccionUpdateView,
    SatisfaccionDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # Clientes
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/crear/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/borrar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # Agentes
    path('agentes/', AgenteListView.as_view(), name='agente_list'),
    path('agentes/crear/', AgenteCreateView.as_view(), name='agente_create'),
    path('agentes/editar/<int:pk>/', AgenteUpdateView.as_view(), name='agente_update'),
    path('agentes/borrar/<int:pk>/', AgenteDeleteView.as_view(), name='agente_delete'),

    # SLA
    path('sla/', SLAListView.as_view(), name='sla_list'),
    path('sla/crear/', SLACreateView.as_view(), name='sla_create'),
    path('sla/editar/<int:pk>/', SLAUpdateView.as_view(), name='sla_update'),
    path('sla/borrar/<int:pk>/', SLADeleteView.as_view(), name='sla_delete'),

    # Tickets
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
    path('tickets/crear/', TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/editar/<int:pk>/', TicketUpdateView.as_view(), name='ticket_update'),
    path('tickets/borrar/<int:pk>/', TicketDeleteView.as_view(), name='ticket_delete'),

    # Interacciones
    path('interacciones/', InteraccionListView.as_view(), name='interaccion_list'),
    path('interacciones/crear/', InteraccionCreateView.as_view(), name='interaccion_create'),
    path('interacciones/editar/<int:pk>/', InteraccionUpdateView.as_view(), name='interaccion_update'),
    path('interacciones/borrar/<int:pk>/', InteraccionDeleteView.as_view(), name='interaccion_delete'),

    # Base de Conocimiento
    path('base_conocimiento/', BaseConocimientoListView.as_view(), name='base_conocimiento_list'),
    path('base_conocimiento/crear/', BaseConocimientoCreateView.as_view(), name='base_conocimiento_create'),
    path('base_conocimiento/editar/<int:pk>/', BaseConocimientoUpdateView.as_view(), name='base_conocimiento_update'),
    path('base_conocimiento/borrar/<int:pk>/', BaseConocimientoDeleteView.as_view(), name='base_conocimiento_delete'),

    # Satisfacción del Cliente
    path('satisfaccion_cliente/', SatisfaccionListView.as_view(), name='satisfaccion_cliente_list'),
    path('satisfaccion_cliente/crear/', SatisfaccionCreateView.as_view(), name='satisfaccion_cliente_create'),
    path('satisfaccion_cliente/editar/<int:pk>/', SatisfaccionUpdateView.as_view(), name='satisfaccion_cliente_update'),
    path('satisfaccion_cliente/borrar/<int:pk>/', SatisfaccionDeleteView.as_view(), name='satisfaccion_cliente_delete'),
]