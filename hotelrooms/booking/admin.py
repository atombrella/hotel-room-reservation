from django.contrib import admin

from hotelrooms.booking.models import Booking, Room


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
