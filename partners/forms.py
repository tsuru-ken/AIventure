from django import forms
from .models import Partners

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partners
        fields = ['name','logo','address','url','established','service','enginner','provision','cost','product','case']