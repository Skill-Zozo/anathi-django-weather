from django import forms

class LoginForm(forms.Form):
	username = forms.EmailField()
	password = forms.CharField(max_length=100)
	
class SignupForm(forms.Form):
	username = forms.EmailField()
	password = forms.CharField(max_length=100)
	confirm_password = forms.CharField(max_length=100)
	
	def clean(self):
		original_password = self.cleaned_data['password']
		confirmed_password = self.cleaned_data['confirm_password']
		
		if original_password != confirmed_password:
			self.add_error('confirm_password', "Passwords not similar")
		