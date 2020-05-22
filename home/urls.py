from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('answer', views.answer, name='answer'),
    path('user', views.user, name='user'),

    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),

	path('reset_password/',
	 auth_views.PasswordResetView.as_view(template_name = "home/password_reset.html"),
	 name = 'reset_password'),

	path('reset_password_sent/',
	 auth_views.PasswordResetDoneView.as_view(template_name = "home/password_reset_sent.html"),
	 name = 'password_reset_done' ),

	path('reset/<uidb64>/<token>/',
	 auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_form.html"),
	 name = 'password_reset_confirm'),

	path('reset_password_complete/',
	 auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_done.html"),
	 name = 'password_reset_complete'),

    
    
]