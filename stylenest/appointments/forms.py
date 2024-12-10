from django import forms
from .models import Booking, Service, SubService

class BookingForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label='Select Service')
    sub_service = forms.ModelChoiceField(queryset=SubService.objects.none(), label='Select Sub-Service')

    class Meta:
        model = Booking
        fields = ['service', 'sub_service', 'date', 'time', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].widget.attrs.update({'class': 'form-control'})
        self.fields['sub_service'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['time'].widget.attrs.update({'class': 'form-control', 'type': 'time'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control', 'rows': 3})

        # Filter sub-services based on selected service
        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                self.fields['sub_service'].queryset = SubService.objects.filter(service_id=service_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['sub_service'].queryset = self.instance.service.subservices.order_by('name')
        if self.instance.pk:  # When editing an existing booking
            self.fields['sub_service'].queryset = self.instance.service.subservices.order_by('name')

