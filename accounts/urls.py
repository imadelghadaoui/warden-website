# accounts/urls.py
from django.urls import path
from .views import user_login

urlpatterns = [
    path('login/', user_login, name='login'),
    # You can add more URLs here like logout, registration, etc.
]
# accounts/urls.py
from django.urls import path
from .views import user_login, user_logout

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # Other URL patterns...
]
