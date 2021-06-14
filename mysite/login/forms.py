from django import forms
from django.contrib.auth.models import User
from django.contrib import messages


class RegisterForm(forms.ModelForm):
    """New user registration form."""

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        """Check if email already exists."""

        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')

        return email

    def clean_username(self):
        """Checks if username already exists within the database."""

        # username = self.cleaned_data.get('username')
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is taken')

        return username

    def clean_password2(self):
        """Validates password and confirmation password."""

        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')

        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
