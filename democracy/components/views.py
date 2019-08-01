from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import *
# Create your views here.


def index(request):
    return render(request,'index.html')



def register_page(request):
    return render(request, 'register_page.html')

def register(request):
    
    try:
        username = request.POST.get('username')
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

        user.save()

        user.set_password(password)

        s_user = SystemUser()
        s_user.user = user
        s_user.user_type = user_type
        s_user.save()


        print(s_user.user_type)
        print(s_user.user_type)
        print(s_user.user_type)
        print(s_user.user_type)
        print(s_user.user_type)


        
        return render(request,'index.html')
    except:
        print("THERE IS A USERNAME CONFLICT")
        print("THERE IS A USERNAME CONFLICT")
        print("THERE IS A USERNAME CONFLICT")
        print("THERE IS A USERNAME CONFLICT")
        return render(request, 'register_page.html')
    
    