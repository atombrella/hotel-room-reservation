from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (
    CreateView, DetailView, FormView, ListView, UpdateView,
)

from .forms import BookingForm, RoomForm
from .models import Booking, Room


class BookRoom(FormView):
    form_class = BookingForm
    template_name = "book_room.html"

    def form_valid(self, form):
        booking = form.instance
        booking.save()
        return HttpResponseRedirect(booking.get_absolute_url())


class BookingView(DetailView):
    model = Booking
    template_name = "book_confirmation.html"
    context_object_name = 'booking'


class Rooms(ListView):
    model = Room
    template_name = 'room_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['rooms'] = Room.objects.all()
        return context


class RoomDetail(DetailView):
    model = Room
    template_name = "book_room.html"


class EditRoomView(UpdateView):
    model = Room
    template_name = "room_edit.html"
    form_class = RoomForm


class CreateRoomView(CreateView):
    model = Room
    template_name = "room_form.html"
    form_class = RoomForm
