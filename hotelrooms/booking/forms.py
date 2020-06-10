from django.contrib.postgres.forms import RangeWidget
from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm, Select

from .models import Booking, Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['floor', 'no']


class BookingForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].empty_label = None

    def save(self, commit=True):
        try:
            return super().save(commit)
        except ValueError as e:
            raise ValidationError(e)

    class Meta:
        model = Booking
        fields = ['room', 'time']
        widgets = {
            'room': Select(attrs={
                'class': 'form-control',
            }),
            'time': RangeWidget(base_widget=DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                },
            )),
        }
