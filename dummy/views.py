  
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             user = form.save()
             login(request, user)
             #  log the user in
             return redirect('dummy:logged')
    else:
        form = UserCreationForm()
    return render(request, 'dummy/signup.html', { 'form': form })

@login_required(login_url="/dummy/login")
def logged(request):
    return render(request,'dummy/logged.html')


@login_required(login_url="/dummy/login")
def balance(request):
    return render(request,'dummy/balance.html')

@login_required(login_url="/dummy/login")
def funds(request):
    return render(request,'dummy/funds.html')

@login_required(login_url="/dummy/login")
def loan(request):
    return render(request,'dummy/loan.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('dummy:logged')
    else:
        form = AuthenticationForm()
    return render(request, 'dummy/login.html', { 'form': form })


def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('dummy:logged')