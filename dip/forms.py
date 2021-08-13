from django import forms
from .models import Columnist,Article
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ColForm(forms.ModelForm):
	class Meta:
		model = Columnist
		fields = '__all__'

class UserFormOmercik(UserCreationForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()

	class Meta:
		model = User
		fields = (
			'first_name',
			'last_name',
			'email',
			'username',
			'password1',
			'password2',
		)