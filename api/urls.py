from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views

from .views import YourModelViewSet, RegisterAPI, LoginAPI, Users


router = routers.DefaultRouter()

router.register(r'yourmodels', YourModelViewSet)
router.register(r'users', Users)

urlpatterns = [
  path('', include(router.urls)),
  path('register/', RegisterAPI.as_view(), name='register'),
  path('login/', LoginAPI.as_view(), name='login'),
  path('logout/', knox_views.LogoutView.as_view(), name='logout'),
  path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
