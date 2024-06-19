
# Create your models here.


# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=True)
    


    


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return self.user