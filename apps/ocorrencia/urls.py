from django.urls import path, include
from rest_framework import routers
from .views import OcorrenciaViewSet 

router = routers.DefaultRouter()
router.register(r'', OcorrenciaViewSet)

urlpatterns = [
    path('', include(router.urls))
]

