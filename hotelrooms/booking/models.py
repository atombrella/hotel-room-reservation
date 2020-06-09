from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields.ranges import (
    DateRangeField, RangeOperators,
)
from django.db import models

from django.urls import reverse

# Maybe you can extend with a Hotel model?


class Room(models.Model):
    floor = models.IntegerField()
    no = models.IntegerField()
    # Perhaps you'd also like to know something about the room, and what
    # it looks like before booking it.

    def __str__(self):
        return f"Room {str(self.floor)}-{str(self.no)}"

    def get_absolute_url(self):
        return reverse("booking:room", kwargs={'pk': self.pk})

    class Meta:
        unique_together = ('floor', 'no'),
        ordering = ('floor', 'no')


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time = DateRangeField(null=False)
    # Perhaps a booking is not always valid?

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
