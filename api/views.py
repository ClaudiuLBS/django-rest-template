from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions
from knox.models import AuthToken
from .serializers import YourModelSerializer, UserSerializer, RegisterSerializer
from .models import YourModel


class YourModelViewSet(viewsets.ModelViewSet):
  queryset = YourModel.objects.all()
  serializer_class = YourModelSerializer

class Users(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })
