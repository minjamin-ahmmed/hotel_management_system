from django.db import models


# Create your models here.
class Room(models.Model):

    room_id = models.IntegerField(primary_key=True)
    rent = models.IntegerField()
    discount = models.IntegerField()
    room_no = models.IntegerField()
    room_type = models.CharField(max_length=20)


