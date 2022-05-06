from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ocorrencia_alt_view),
    path('<uuid:id_ocorrencia>/', views.ocorrencia_alt_view),
]

