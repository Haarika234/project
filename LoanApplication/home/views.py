from django.shortcuts import render
from django.http import HttpResponse
from home.forms import ProfileForm, FinancialForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, "home/home.html", context={})

@login_required
def Profile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect(reverse('home:financial'))
        else:
            messages.warning(request, "details are wrong!!!")
    return render(request, "home/profile.html", context={"form":form})

def Financial(request):
    form = FinancialForm()
    if request.method == "POST":
        form = FinancialForm(request.POST)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return HttpResponseRedirect(reverse('home:home'))
        else:
            messages.warning(request, "details are wrong!!!")
    return render(request, "home/financial.html", context={"form":form})
