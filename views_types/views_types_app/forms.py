from django import forms
from .models import Geeksmodel

class GeeksForm(forms.ModelForm):
    class Meta:
        model = Geeksmodel
        fields = [
            "title",
            "description",
        ]