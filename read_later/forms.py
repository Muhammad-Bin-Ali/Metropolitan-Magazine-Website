from django import forms
from .models import ReadLater

class Populate_ReadLater(forms.ModelForm):
	
    class Meta:
        model = ReadLater
        fields = ["user", "post"]