from django.contrib.auth.models import User
from django.urls import path, include
from .views import YourModelViewSet, RegisterAPI, Users
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'yourmodels', YourModelViewSet)
router.register(r'users', Users)

urlpatterns = [
  path('', include(router.urls)),
  path('register/', RegisterAPI.as_view(), name='register' )
]
