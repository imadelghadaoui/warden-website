from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
