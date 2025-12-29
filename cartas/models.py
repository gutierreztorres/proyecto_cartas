import uuid
from django.db import models

class Carta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destinatario = models.CharField(max_length=100)
    contenido = models.TextField()
    creada_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carta para {self.destinatario}"