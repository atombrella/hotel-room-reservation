from django.views.generic import FormView, ListView

from .forms import RoomForm
from .models import Room


class BookRoom(FormView):
    form_class = RoomForm


class Rooms(ListView):
    model = Room
    template_name = 'room_list.html'
