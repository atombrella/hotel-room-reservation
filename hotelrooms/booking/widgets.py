from django.forms import DateInput


class BootstrapDateTimePickerInput(DateInput):
    template_name = 'widgets/bootstrap_datetimepicker.html'
