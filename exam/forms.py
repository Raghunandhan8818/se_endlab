from exam.models import *
from django import forms
from django.forms import ModelForm


class ExamForm(ModelForm):
    box_1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter Your Project Title",
    }))
    box_2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter Your Project Title",
    }))
    box_3 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter Your Project Title",
    }))

    class Meta:
        model = FirstModel
        fields = ['box_1', 'box_2', 'box_3']
