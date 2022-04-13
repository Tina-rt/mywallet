from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import WalletUser
from django.core import serializers
from django.forms.models import model_to_dict


def isLogged(request):
    return 'user' in request.session
        

def index(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        current_user = WalletUser.objects.filter(username = username).first()
        if current_user.password == password:
            user_serialised = model_to_dict(current_user)
            user_serialised['amount'] = float(user_serialised['amount'])
            request.session['user'] = user_serialised
            
            return redirect(home)
        else:
            return redirect(index)
        
    else:
        if isLogged(request):
            return redirect(home)
            # return redirect(home)
        
    
    return render(request, 'mywallet/login.html')

def logout(request):
    try:
        del request.session['user']
    except:
        pass
    return redirect(index)

def home(request):
    if isLogged(request):
        current_user = request.session['user']
        return render(request, 'mywallet/home.html', current_user)
    else:
        return redirect(index)

def transfer(request):
    if request.method == 'POST':
        username_dest = request.POST['username_dest']
        amount = request.POST['amount']
        current_user = WalletUser.objects.filter(username = request.session['user']['username']).first()
        if current_user.amount >= float(amount):
            return render(request, 'mywallet/home.html', context={
                'message': 'success'
            })
        else:
            return render(request, 'mywallet/home.html', context={
                "message": "NO"
            })
    else:
        return render(request)

def deposit(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'mywallet/deposit.html')

def register(request):
    if request.method == 'POST':
        u = WalletUser(
            name = request.POST['name'],
            first_name = request.POST['firstname'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        print(u)
        u.save()
        return redirect(index)
    else:
        return render(request, 'mywallet/register.html')
    return render(request, 'mywallet/register.html')
# Create your views here.
