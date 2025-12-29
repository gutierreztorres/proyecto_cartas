from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RespuestaForm

def responder_view(request):
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por tu respuesta!')
            return redirect('responder') # Redirige a donde quieras después de enviar
    else:
        form = RespuestaForm()
    
    return render(request, 'respuesta/respuesta.html', {'form': form})