from django import forms
from .models import Tip

class Tip(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Tip.objects.all())
