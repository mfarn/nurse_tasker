from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
   path('', views.prescricao_alt_view),
   path('<uuid:id_prescricao>/', views.prescricao_alt_view),
   path('<str:usuario>/', views.prescricao_alt_view),
]
