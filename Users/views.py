from django.shortcuts import render, redirect
#from django.views.generic import Login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import UserRegForm
# Create your views here.

class MyLoginView(LoginView):
    template_name = "Users/login.html"

class MyLogoutView(LogoutView):
    template_name = "Users/logout.html"

# class RegView(CreateView):
#     model = User
#     form = UserRegForm()
#     template_name = "Users/register.html"

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
#            messages.success(request, f'Account created for {username}! You can login now')
            return redirect('login-page')
    else:
        form = UserRegForm()
    return render(request, 'users/register.html', {'form': form})
