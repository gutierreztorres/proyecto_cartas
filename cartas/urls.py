from django.urls import path
from . import views

urlpatterns = [
    # La URL se verá algo como: tuweb.com/carta/550e8400-e29b-41d4-a716-446655440000
    path('carta/<uuid:pk>/', views.detalle_carta, name='detalle_carta'),
]