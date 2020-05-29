from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields.ranges import DateRangeField, RangeOperators
from django.db import models


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
            ExclusionConstraint(
                name='hotel_room_excl_constraint',
                expressions=[("time", RangeOperators.OVERLAPS)],
                index_type="GIST",
            )
        ]
