from django.db import models

# Create your models here.
type_id = models.IntegerField(primary_key=True)
type_name = models.CharField(max_length = 20)
description = models.CharField(max_length = 200)