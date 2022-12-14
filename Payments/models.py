from django.db import models
from Booking.models import Booking

# Create your models here.
class Payments(models.Model):
    payment_id = models.IntegerField(primary_key = True)
    payment_method = models.CharField(max_length = 15)

    booking_id = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True)
