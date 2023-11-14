from .models import Parrot
from django.forms import ModelForm, fields, widgets, TextInput, Textarea, ImageField


class ParrotForm(ModelForm):
    class Meta:
        model = Parrot
        fields = [
            "name",
            "description",
            "avatar"
        ]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter parrot name"
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter parrot descripton"
            })
        }