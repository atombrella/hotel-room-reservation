from django.views import View
from django.views.generic import ListView, TemplateView

from .forms import RoomForm
from .models import Room


class Index(TemplateView):
    template_name = "booking_index.html"


# class BookRoom(FormView):
#     form_class = RoomForm


class Rooms(ListView):
    model = Room
    template_name = 'room_list.html'
