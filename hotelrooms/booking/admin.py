from django.contrib import admin

from .forms import BookingForm
from .models import Booking, Room


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    form = BookingForm

    class Media:
        css = {
            "all": (
                "bootstrap/css/bootstrap.min.css",
            )
        }
        js = (
            "bootstrap/js/bootstrap.min.js",
            "js/bootstrap-datetimepicker.min.js",
        )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
