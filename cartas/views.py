from django.shortcuts import render, get_object_or_404
from .models import Carta

def detalle_carta(request, pk):
    # Busca la carta por su UUID (pk)
    carta = get_object_or_404(Carta, pk=pk)
    return render(request, 'cartas/detalle.html', {'carta': carta})