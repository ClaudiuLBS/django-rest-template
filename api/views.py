from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelViewSet(viewsets.ModelViewSet):
  queryset = YourModel.objects.all()
  serializer_class = YourModelSerializer
