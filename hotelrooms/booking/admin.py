from django.contrib import admin
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import IntegrityError, transaction
from django.forms import ModelForm

from .forms import BookingForm
from .models import Booking, Room


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    form = BookingForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=obj, **kwargs)
        # It won't be displayed correctly without this!
        form.base_fields['time'].initial = [obj.time.lower, obj.time.upper]
        return form

    def save_form(self, request, form, change):
        return super().save_form(request, form, change)

    def save_model(self, request, obj: Booking, form: ModelForm, change: bool):
        try:
            super().save_model(request, obj, form, change)
        except IntegrityError:
            form.add_error(NON_FIELD_ERRORS, "The room is already booked on some of those days")

    class Media:
        css = {
            "all": (
                "bootstrap/css/bootstrap.min.css",
            )
        }
        js = (
            "bootstrap/js/bootstrap.min.js",
        )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
