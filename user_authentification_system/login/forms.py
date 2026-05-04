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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })      
        self.fields['phone_number'].widget.attrs.update({
            'placeholder': '+257 XX XX XX XX'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'account@xyz.com'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password'
        })      
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm your password'
        })
