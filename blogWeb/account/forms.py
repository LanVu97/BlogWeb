from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import User



# Create your forms here.

class UserForm(UserCreationForm):
	# email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")


	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

