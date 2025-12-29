from django import forms
from .models import Respuesta

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['nombre', 'texto']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Escribe tu nombre...', 'class': 'input-carta'}),
            'texto': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje...', 'rows': 5}),
        }