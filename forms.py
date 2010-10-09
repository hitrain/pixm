from django import forms


class Email(forms.Form):
	email = forms.EmailField()
	