from django import forms
from .models import Faculty

class Facultyform(forms.ModelForm):
    class Meta:
        Model=Faculty
        Fields='__all__'