from django.db import models

class Respuesta(models.Model):
    nombre = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self):
        return f"Respuesta de {self.nombre}"