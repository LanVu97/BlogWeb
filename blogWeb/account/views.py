from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.forms import UserForm
from account.models import User

def register_request(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)			
			messages.success(request, "Registration successful." )
			return redirect('home')
	else:
		form = UserForm()
	return render (request, 'account/register.html', {'form': form})


def login_request(request):
	
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		
		user = authenticate( email=email, password = password)
			
		if user is not None:
				login(request, user)
				if request.GET.get('next') :				
					return redirect(request.GET.get('next'))
				else:
					messages.success(request, f' welcome, {user.username} !!!')
					return redirect('home')
				
		else:
				messages.warning(request, f'Please check your email or password again')
				return redirect('login')


	return render (request, 'account/login.html')

@login_required(login_url='login')
def logout_request(request):
	logout(request)
	messages.success(request, "You have successfully logged out.") 
	return redirect('home')