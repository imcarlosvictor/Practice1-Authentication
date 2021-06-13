from django.shortcuts import render

from .forms import RegisterForm


# Create your views here.
def login_request(request):
    pass


def logout_request(request):
    pass


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            cd = register_form.cleaned_data

    else:
        register_form = RegisterForm()
    return render(request, 'main/dashboard.html',
                  {'register_form': register_form})


def dashboard(request):
    pass
