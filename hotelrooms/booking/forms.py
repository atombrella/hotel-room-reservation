from django.contrib.postgres.forms import RangeWidget
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db import IntegrityError, connection, transaction
from django.forms import DateInput, ModelForm, Select

from .models import Booking, Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class BookingForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].empty_label = None

    def clean(self):
        if hasattr(self.instance, "pk"):
            with transaction.atomic() as t:
                self.instance.time = self.cleaned_data['time']
                try:
                    self.instance.save()
                except IntegrityError:
                    raise ValidationError("Can't book hotel room on the same day")
        return self.cleaned_data

    class Meta:
        model = Booking
        fields = '__all__'
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
