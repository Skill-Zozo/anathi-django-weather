from django.shortcuts import render
from .forms import LoginForm
from .forms import SignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
	form = LoginForm()
        return render(request, 'weather/home.html', {'form': form})

def loginUser(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['username']
			pwd = form.cleaned_data['password']
			user = authenticate(username=email, password=pwd)
			if user is not None:
				login(request, user)
			return HttpResponseRedirect('/actual_weather/')
	return render(request, 'weather/home.html', {'form': form})

def signup(request):
	form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['username']
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			user = User.objects.create_user(email, email, password)
			return HttpResponseRedirect('/actual_weather/')
	return render(request, 'weather/signup.html', {'form': form})
	
def register(request):
    return render(request,'weather/basic.html')
def actual_weather(request):
	return render(request,'weather/actual_weather.html')
def logout_view(request):
    form = LoginForm()
    logout(request)
    return HttpResponseRedirect('/login/')
