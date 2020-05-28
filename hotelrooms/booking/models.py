from django.contrib.postgres.constraints import ExclusionConstraint
from django.db import models


class Room(models.Model):
    floor = models.IntegerField()
    no = models.IntegerField()
    description = models.TextField()

    class Meta:
        unique_together = ('floor', 'no'),
    

class Booking(models.Model):
    
    
