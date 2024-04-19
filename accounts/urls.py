# accounts/urls.py
from django.urls import path
from .views import register, homepage
from .views import user_login, user_logout

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('home/', homepage, name='homepage'),
   
]
