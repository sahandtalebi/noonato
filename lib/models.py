from django.utils import timezone
from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_time

