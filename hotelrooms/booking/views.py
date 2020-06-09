from django.views.generic import (
    CreateView, DetailView, FormView, ListView, UpdateView,
)

from .forms import BookingForm, RoomForm
from .models import Room


class BookRoom(FormView):
    form_class = BookingForm

    def get_template_names(self):
        return "book_room.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = context['rooms'] = Room.objects.all()
        return context

    def get_form_kwargs(self, **kwargs):
        try:
            return {
                'room': Room.objects.get(pk=self.kwargs['pk']),
                **kwargs,
            }
        except Exception:  # make more specific
            return None


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
