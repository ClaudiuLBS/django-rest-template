from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import YourModel


class YourModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = YourModel
    fields = ('__all__')