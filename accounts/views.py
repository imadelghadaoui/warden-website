# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to dashboard or any other page after login
                return redirect('dashboard')  # Assuming 'dashboard' is the name of your dashboard URL pattern
            else:
                # Invalid login
                return render(request, 'accounts/login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# accounts/views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout
