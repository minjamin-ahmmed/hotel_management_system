from django.db import models
from Room.models import Room


# Create your models here.
class Booking(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    date_from = models.DateField()
    date_to = models.DateField()

    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)