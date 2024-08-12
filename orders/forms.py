from django import forms
from .models import *

class order_form(forms.ModelForm):
    class Meta:
        model = order_model
        fields = ['invoice','first_name', 'last_name', 'phone', 'email', 'country', 'state', 'street', 'building', 'house', 'postal', 'cardno', 'expiry', 'cvv']
    