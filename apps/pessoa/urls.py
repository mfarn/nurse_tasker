from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('usuarios', views.usuario_alt_view),
    path('pacientes', views.paciente_alt_view),
    path('usuarios/<str:CPF>/', views.usuario_alt_view),
    path('pacientes/<str:CPF>/', views.paciente_alt_view),
]

