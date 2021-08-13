from django import forms
from .models import Columnist,Article


class ColForm(forms.ModelForm):
	class Meta:
		model = Columnist
		fields = '__all__'

