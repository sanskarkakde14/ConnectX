from django import forms
from .models import Lead


class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'phone', 'Address', 'property_price', 'property_size', 'property_locality', 'property_type', 'priority')


