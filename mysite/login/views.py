from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm


# Create your views here.
def login_request(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main/dashboard.html',
                                  {'user': user})
                else:
                    return HttpResponse('Disabled account')
            else:
                messages.error(request, 'Invalid login')
    else:
        login_form = LoginForm()

    context = {'login_form': login_form}
    return render(request, 'registration/login.html', context)


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # Create new user but don't save just yet
            user = register_form.save(commit=False)
            # Set user password
            user.set_password(register_form.cleaned_data['password'])
            # Save user
            user.save()
            # Success message
            context = {'user': user}
            return render(request, 'main/dashboard.html', context)
        else:
            messages.error(request, 'Account invalid')
    else:
        register_form = RegisterForm()

    context = {'register_form': register_form}
    return render(request, 'registration/register.html', context)


@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')
