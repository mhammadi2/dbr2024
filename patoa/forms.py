from django import forms
from django.core.validators import MaxValueValidator, MinLengthValidator
from .models import Patent
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class PatentForm(forms.Form):
    A112 = forms.BooleanField(label= "112 Rejection",required=False)
    obj = forms.BooleanField(label= "Objection",required=False)
    spec = forms.BooleanField(label= "Specfication",required=False)
    drw = forms.BooleanField(label= "Drawing",required=False)
    A102103 = forms.BooleanField(label= "102 & 103 Rejection",required=False)


class PatForm(forms.ModelForm):
    class Meta:
        model = Patent
        fields = ['patnof']
        labels = {
            'patnof': "Pat Application or PGpub Number:",
        }
