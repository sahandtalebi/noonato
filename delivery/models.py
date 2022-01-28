from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.

class Delivery(User):
    delivery_count = models.IntegerField(default=0, verbose_name='تعداد سفارشات')

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'پیک'
        verbose_name_plural = 'پیک ها'
