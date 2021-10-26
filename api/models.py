from django.db import models
from django.db.models.fields import CharField, IntegerField

class YourModel(models.Model):
  name = CharField(max_length=50, default='name')
  some_number = IntegerField(default=69)

  def __str__(self) -> str:
      return self.name