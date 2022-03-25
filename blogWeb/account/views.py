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


def login_request(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate( email=email, password = password)
		if user is not None:
			login(request, user)
			messages.success(request, f' welcome, {user.username} !!!')
			return render(request,'index.html')
			
		else:
			messages.warning(request, f'account done not exit plz sign in')
			return redirect('login')

	return render (request, 'account/login.html')

def logout_request(request):
	logout(request)
	messages.success(request, "You have successfully logged out.") 
	return render(request,'index.html')