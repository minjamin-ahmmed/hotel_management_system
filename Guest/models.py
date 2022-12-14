from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Guest(models.Model):
    guest_number = models.IntegerField(primary_key=True)
    guest_name = models.CharField(max_length=50)
    guest_address = models.CharField(max_length=100)
    guest_country = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)