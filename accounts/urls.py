"""orphansys2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [

    # Django default authentication generic views
    # path('', auth_views.LoginView.as_view(template_name='authentication/login.html',
    #      redirect_authenticated_user=True), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html',
    #      redirect_authenticated_user=True), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(
    #     template_name='authentication/logout.html'), name='logout'),

    # Custom views and URLs for authentication
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),

    # Password reset generic views and URLs (using custom HTML templates)
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="password_reset/password_reset.html",
        html_email_template_name="password_reset/password_reset_email.html",
        email_template_name='password_reset/password_reset_email.html',
        subject_template_name="password_reset/password_reset_subject.txt"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset/password_reset_done.html"), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset/password_reset_complete.html"), name="password_reset_complete"),

    # Password reset generic views and URLs (using Django admin default)
    # path("password_reset/", auth_views.PasswordResetView.as_view(
    #     html_email_template_name="password_reset/password_reset_email.html",
    #     email_template_name='password_reset/password_reset_email.html',
    #     subject_template_name="password_reset/password_reset_subject.txt"), name="password_reset"),
    # path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
    # ), name="password_reset_done"),
    # path("password_reset_confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(
    # ), name="password_reset_confirm"),
    # path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(
    # ), name="password_reset_complete"),
]
