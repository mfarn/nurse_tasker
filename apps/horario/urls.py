from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
   path('', views.horario_alt_view),
   path('<uuid:id_horario>', views.horario_alt_view),
]
