from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.handleLogin, name='login'),
    path('signup', views.handleSignup, name='signup'),
    path('logout', views.handleLogout, name='logout'),
    path('blog/<str:slug>', views.blog, name='blogPost'),
    path('create-blog', views.createBlog, name='createBlog'),
]