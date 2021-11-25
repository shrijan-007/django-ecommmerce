from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,PasswordResetForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms.widgets import TextInput

# from django.forms import fields
# from django.forms.models import _Labels



class userRegistrationForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'autocomplete':'off'}))
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'autocomplete':"off"}),label='Password')
    password2 = forms.CharField(widget = forms.PasswordInput(),label='Confirm Password')
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class loginForm(AuthenticationForm):
    # email = forms.EmailField(required=True)
    username = UsernameField(widget = forms.TextInput(attrs={'autofocus': True}),label="Username")
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )