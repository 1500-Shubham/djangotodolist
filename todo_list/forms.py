from django import forms
from .models import list

class listforms(forms.ModelForm):
	class Meta:
		model=list #model class se list object
		fields=["item","completed"]