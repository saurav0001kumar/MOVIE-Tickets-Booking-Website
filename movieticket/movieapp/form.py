from movieapp.models import reg
from django import forms

class regForm(forms.ModelForm):
    class Meta:
        model=reg
        fields="__all__"
