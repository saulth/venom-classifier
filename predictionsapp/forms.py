from django import forms
from . import models

class sequenceForm(forms.ModelForm):
    class Meta:
        model = models.Sequences
        fields = ['sequence',]