from django.urls import path, include
from rest_framework import routers
from .views import PrescricaoViewSet
 
router = routers.DefaultRouter()
router.register(r'', PrescricaoViewSet)
 
urlpatterns = [
   path('', include(router.urls))
]
