from datetime import date

from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields.ranges import (
    DateRangeField, RangeOperators,
)
from django.core.exceptions import ValidationError
from django.db import IntegrityError, models

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

    def __str__(self):
        return f"{self.room} booked from {self.time.lower} to {self.time.upper}"

    def get_absolute_url(self):
        return reverse("booking:booking", kwargs={'pk': self.pk})

    def full_clean(self, exclude=None, validate_unique=True):
        return super().full_clean(exclude, validate_unique)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # Check how the current values differ from ._loaded_values. For example,
        # prevent changing the creator_id of the model. (This example doesn't
        # support cases where 'creator_id' is deferred).
        try:
            super().save(force_insert, force_update, using, update_fields)
        except IntegrityError:
            raise ValueError("There's already a booking for the room on those days!")

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
