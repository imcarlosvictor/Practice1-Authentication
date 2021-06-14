from django.urls import path

from . import views

urlpatterns = [
    # Authentication Views
    path('', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.dashboard, name='dashboard'),
]
