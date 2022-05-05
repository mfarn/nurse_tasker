from django.urls import path, include
from rest_framework import routers
from .views import HorarioViewSet
 
router = routers.DefaultRouter()
router.register(r'', HorarioViewSet)
 
urlpatterns = [
   path('', include(router.urls))
]
