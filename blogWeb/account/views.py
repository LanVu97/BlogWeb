from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from account.forms import UserForm

def register_request(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)			
			messages.success(request, "Registration successful." )
			return render(request,'index.html')
	else:
		form = UserForm()
	return render (request, 'account/register.html', {'form': form})

