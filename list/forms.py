from django import forms
from .models import Insta


class ListForm(forms.ModelForm):
    class Meta:
        model=Insta
        fields=[
            'kuladi',
        ]
