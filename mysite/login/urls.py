from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Authentication Views
    path('', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('password_change/', auth_views.PasswordChangeView.as_view()),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view()),
    path('password_reset/', auth_views.PasswordResetView.as_view()),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view()),
    path('password_reset_confirm/',
         auth_views.PasswordResetConfirmView.as_view()),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view()),

    # My Views
    path('register/', views.register, name='register'),
    path('profile/', views.dashboard, name='dashboard'),
]
