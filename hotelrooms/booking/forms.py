from django.contrib.postgres.forms import RangeWidget
from django.forms import DateInput, ModelForm, Select

from .models import Booking, Room

from .widgets import BootstrapDateTimePickerInput


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['floor', 'no']


class BookingForm(ModelForm):

    def __init__(self, room, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].initial = room
        self.fields['room'].empty_label = None

    class Meta:
        model = Booking
        fields = ['room', 'time']
        widgets = {
            'room': Select(attrs={
                'class': 'form-control'
            }),
            'time': RangeWidget(base_widget=BootstrapDateTimePickerInput(
                attrs={
                    'class': 'form_datetime',
                },
            )),
        }
