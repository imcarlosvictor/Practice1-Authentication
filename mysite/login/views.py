from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import LoginForm, RegisterForm


# Create your views here.
def login_request(request):
    if request.method == "POST":
        login_form = LoginForm()
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                return render(request, 'main/dashboard.html')
            else:
                pass
    else:
        login_form = LoginForm()

    return render(request, 'registration/login.html',
                  {"login_form": login_form})


def logout_request(request):
    pass


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # Create new user but don't save just yet
            new_user = register_form.save(commit=False)
            # Set user password
            new_user.set_password(register_form.cleaned_data['password2'])
            # Save user
            new_user.save()
            return render(request, 'main/dashboard.html',
                          {'new_user': new_user})
    else:
        register_form = RegisterForm()

    return render(request, 'registration/register.html',
                  {'register_form': register_form})


def dashboard(request):
    pass
