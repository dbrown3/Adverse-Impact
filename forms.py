from django import forms
from django.forms.widgets import Input

class DataEntryForm(forms.Form):
    xml_file = forms.FileField()