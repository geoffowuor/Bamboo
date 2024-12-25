from django import forms
from .models import booking,reserve

class bookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'

class reserveForm(forms.ModelForm):
    class Meta:
        model = reserve
        fields = '__all__'
