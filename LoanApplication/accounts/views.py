from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignupForm, LoginForm
from .models import CustomUser
from django.http import HttpResponseRedirect

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Save user without committing to the database yet
            user = form.save(commit=False)

            # Set password from the form data
            user.set_password(form.cleaned_data['password'])

            # Save user to the database
            user.save()

            # Log the user in immediately after saving
            login(request, user)

            # Success message
            messages.success(request, "Account created successfully. You are now logged in.")

            # Redirect to login page (or any other page you want)
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            # If form is not valid, print form errors for debugging
            print(form.errors)
    else:
        # Initialize an empty form for GET requests
        form = SignupForm()

    # Render the signup page with the form
    return render(request, 'accounts/signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return HttpResponseRedirect(reverse("home:home")) # Redirect to home or dashboard page
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})