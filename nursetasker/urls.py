"""nursetasker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from pessoa.api import viewsets as pessoaviewsets
from prescricao.api import viewsets as prescricaoviewsets
from horario.api import viewsets as horarioviewsets
from ocorrencia.api import viewsets as ocorrenciaviewsets
route = routers.DefaultRouter()

route.register(r'usuarios', pessoaviewsets.UsuarioViewSet, basename='usuarios')
route.register(r'pacientes', pessoaviewsets.PacienteViewSet, basename='pacientes')
route.register(r'prescricao', prescricaoviewsets.PrescricaoViewSet, basename='prescricao')
route.register(r'horarios', horarioviewsets.HorarioViewSet, basename='horarios')
route.register(r'ocorrencia', ocorrenciaviewsets.OcorrenciaViewSet, basename='ocorrencia')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
