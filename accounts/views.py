# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import CustomUserCreationForm  # Import your custom form


class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.username  # Set email as the same value as username
            user.save()
            login(request,user)
            return redirect('home')
        return render(request, 'accounts/signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

        return render(request, 'accounts/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
