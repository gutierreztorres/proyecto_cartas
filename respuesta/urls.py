from django.urls import path
from . import views

urlpatterns = [
    path('responder/', views.responder_view, name='responder'),
]