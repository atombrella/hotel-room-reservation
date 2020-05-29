from django.views.generic import ListView

from hotelrooms.booking.models import Room


class Rooms(ListView):
    model = Room
    template_name = 'room_list.html'
