from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,PasswordResetForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms.widgets import TextInput
from .models import States_choice

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

class customers_Adress(forms.Form):
    fname = forms.CharField(label="First Name")
    lname = forms.CharField(label="Last Name")
    phoneNo = forms.IntegerField(label="Phone No.")
    address = forms.CharField(label="Address")
    state = forms.ChoiceField(label = "State",choices=States_choice, required=True)
    pincode = forms.CharField(label = "Pincode",max_length=10)

class changeUserPass(PasswordChangeForm):
    old_password = forms.CharField(
        label=("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label=("Confirm new password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    class Meta:
        model = User

        field_order = ['old_password', 'new_password1', 'new_password2']