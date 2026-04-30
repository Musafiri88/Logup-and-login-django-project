from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    ''' User sign up form '''
    email = forms.EmailField(required=True)

    class Meta:
        ''' class Meta '''
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
