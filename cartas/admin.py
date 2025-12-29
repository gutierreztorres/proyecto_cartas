from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Carta

@admin.register(Carta)
class CartaAdmin(admin.ModelAdmin):
    # Columnas que se verán en la lista
    list_display = ('destinatario', 'creada_el', 'ver_carta_link')
    
    # Campo de solo lectura para ver el ID en el detalle
    readonly_fields = ('id',)

    # Función para crear el botón/enlace
    def ver_carta_link(self, obj):
        # Genera la URL usando el nombre que pusimos en urls.py
        url = reverse('detalle_carta', args=[obj.pk])
        return format_html('<a class="button" href="{}" target="_blank">Abrir Carta</a>', url)
    
    ver_carta_link.short_description = 'Enlace Público'