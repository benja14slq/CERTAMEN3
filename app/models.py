from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Evento(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    TIPO_CHOICES = [
        ('Vacaciones', 'Vacaciones'),
        ('Feriado', 'Feriado'),
        ('Suspensión de actividades', 'Suspensión de actividades'),
        ('Suspensión de actividades PM', 'Suspensión de actividades PM'),
        ('Periodo Lectivo', 'Periodo Lectivo'),
        ('Suspensión de evaluaciones', 'Suspensión de evaluaciones'),
        ('Ceremonio', 'Ceremonio'),
        ('EDDA', 'EDDA'),
        ('Evaluación', 'Evaluación'),
        ('Ayudantías', 'Ayudantías'),
        ('Hito Académico', 'Hito Académico'),
        ('Secretaria Académica', 'Secretaria Académica'),
        ('OAI', 'OAI'),
    ]
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    SEGMENTOS_CHOICES = [
        ('Comunidad USM', 'Comunidad USM'),
        ('Estudiante', 'Estudiante'),
        ('Profesor', 'Profesor'),
        ('Jefe de Carrera', 'Jefe de Carrera'),
    ]
    segmento = models.CharField(max_length=30, choices=SEGMENTOS_CHOICES)
