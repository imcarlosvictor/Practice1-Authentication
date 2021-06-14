from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Authentication Views
    path('', views.login_request, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.dashboard, name='dashboard'),
]
