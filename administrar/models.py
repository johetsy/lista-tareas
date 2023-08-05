from django.db import models

# Create your models here.
class Tarea(models.Model):
  titulo = models.CharField(max_length=64, blank = False, null = False, default = "---")
  # estado 1 = tarea pendiente y Estado 0 = tarea finalizada
  estado = models.BooleanField(default = 0)
  