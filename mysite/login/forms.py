from django import forms

from .models import Person


class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'gender']
