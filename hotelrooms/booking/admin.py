from django.contrib import admin
from django.core.exceptions import ValidationError

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

    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except ValueError as e:
            print(e)
            form.errors['__all__'] = "The room is already booked on some of those days"

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
