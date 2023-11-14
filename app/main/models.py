from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

# Create your models here.
class Parrot(ExportModelOperationsMixin("dataset"),models.Model):
    name = models.CharField("Имя", max_length=32)
    description = models.TextField("Описание")
    avatar = models.ImageField(upload_to='uploads/', default="images/default.jpg")

    def __str__(self):
        return self.name
