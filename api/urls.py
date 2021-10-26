from django.urls import path, include
from .views import YourModelViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'YourModel', YourModelViewSet)

urlpatterns = [
  path('', include(router.urls))
]
