from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    """New user registration form."""

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def validate_password(self):
        """Validates password and confirmation password."""

        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')

        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
