from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return render(request,'index.html')



def register_page(request):
    return render(request, 'register_page.html')

def register(request):
    
    try:
        username = request.POST.get('username').lower()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user_type = request.POST.get('type')
        password = request.POST.get('password')
        
        user = User()
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.set_password(password)
        user.save()

        

        s_user = SystemUser()
        s_user.user = user
        s_user.user_type = user_type
        s_user.save()


        


        
        return render(request,'index.html')
    except:
        
        return render(request, 'register_page.html')



@csrf_exempt
def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    context = {}
    if user is not None:
        login(request,user)
        context['user'] = SystemUser.objects.get(user=user)
        Suser = context['user']
        if Suser.user_type is 'M':
            return render(request, 'manager_page.html', context)
        elif Suser.user_type is 'R':
            return render(request, 'user_page.html', context)

    else:
        return render(request, 'index.html')


def logout_page(request):
    logout(request)
    return redirect('index.html')
    
