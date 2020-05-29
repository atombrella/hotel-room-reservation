from django.forms import ModelForm

from .models import Room


class RoomForm(ModelForm):
    model = Room
