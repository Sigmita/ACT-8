from django.db import models

class ClienteSoporte(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=255)
    contacto_principal = models.CharField(max_length=100)
    email_contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    sector_empresa = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    nivel_soporte = models.CharField(max_length=50)
    sitio_web = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_empresa

class AgenteSoporte(models.Model):
    id_agente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    nivel_experiencia = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class SLA(models.Model):
    id_sla = models.AutoField(primary_key=True)
    nombre_sla = models.CharField(max_length=100)
    descripcion = models.TextField()
    tiempo_respuesta_horas = models.IntegerField()
    tiempo_resolucion_horas = models.IntegerField()
    prioridad_asociada = models.CharField(max_length=20)
    penalizacion_incumplimiento = models.TextField()
    es_activo = models.BooleanField()

    def __str__(self):
        return self.nombre_sla

class BaseConocimiento(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    titulo_articulo = models.CharField(max_length=255)
    contenido_articulo = models.TextField()
    fecha_publicacion = models.DateTimeField()
    autor = models.CharField(max_length=100)
    categoria_articulo = models.CharField(max_length=50)
    palabras_clave = models.TextField()
    veces_consultado = models.IntegerField()
    es_publico = models.BooleanField()

    def __str__(self):
        return self.titulo_articulo

class TicketSoporte(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField()
    estado = models.CharField(max_length=50)
    prioridad = models.CharField(max_length=20)
    cliente = models.ForeignKey(ClienteSoporte, on_delete=models.CASCADE)
    agente_asignado = models.ForeignKey(AgenteSoporte, on_delete=models.SET_NULL, null=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    tipo_incidente = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    resolucion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Ticket #{self.id_ticket} - {self.titulo}"

class Interaccion(models.Model):
    id_interaccion = models.AutoField(primary_key=True)
    ticket = models.ForeignKey(TicketSoporte, on_delete=models.CASCADE)
    agente = models.ForeignKey(AgenteSoporte, on_delete=models.CASCADE)
    fecha_interaccion = models.DateTimeField()
    tipo_interaccion = models.CharField(max_length=50)
    descripcion_interaccion = models.TextField()
    archivos_adjuntos = models.TextField(null=True, blank=True)
    duracion_minutos = models.IntegerField()

class SatisfaccionCliente(models.Model):
    id_encuesta = models.AutoField(primary_key=True)
    ticket = models.ForeignKey(TicketSoporte, on_delete=models.CASCADE)
    fecha_encuesta = models.DateTimeField()
    calificacion_agente = models.IntegerField()
    calificacion_resolucion = models.IntegerField()
    comentarios_cliente = models.TextField(null=True, blank=True)
    fecha_envio = models.DateTimeField()
    fue_resuelto = models.BooleanField()
