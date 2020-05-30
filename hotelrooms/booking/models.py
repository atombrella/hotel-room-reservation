from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields.ranges import (
    DateRangeField, RangeOperators,
)
from django.db import models

# Maybe you can extend with a Hotel model?


class Room(models.Model):
    floor = models.IntegerField()
    no = models.IntegerField()

    def __str__(self):
        return f"Room {str(self.floor)}-{str(self.no)}"

    class Meta:
        unique_together = ('floor', 'no'),


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time = DateRangeField()
    # perhaps a booking is not always valid?

    class Meta:
        constraints = [
            ExclusionConstraint(
                name='hotel_room_excl_constraint',
                expressions=[
                    ("time", RangeOperators.OVERLAPS),
                    ("room", RangeOperators.EQUAL),
                ],
                index_type="GIST",
            )
        ]
