from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields.ranges import DateRangeField
from django.db import models
from django.db.models import F


class Room(models.Model):
    floor = models.IntegerField()
    no = models.IntegerField()

    class Meta:
        unique_together = ('floor', 'no'),


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time = DateRangeField()

    class Meta:
        constraints = [
            ExclusionConstraint(expressions=[F("time")], index_type="GIST")
        ]
