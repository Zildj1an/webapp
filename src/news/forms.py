from django import forms

from .models import Regis

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Regis
		fields = ["name", "email"]

	def clean_email(self):
		email  = self.cleaned_data.get("email")
		return email

class ContactForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField(widget= forms.Textarea)
