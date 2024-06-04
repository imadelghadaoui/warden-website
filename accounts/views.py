from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home.html')

def thank_you(request):
    return render(request, 'thank_you.html')
from .models import ContactFormSubmission

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Save form data to database
            submission = ContactFormSubmission(name=name, email=email, phone=phone, message=message)
            submission.save()
            
            
            return redirect('thank_you')  # Redirect to thank you page
    else:
        form = ContactForm()
    
    return render(request, 'contact_us.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard_home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth_logout(request)
    return redirect('home')


