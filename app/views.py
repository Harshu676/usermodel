from django.shortcuts import render

# Create your views here.

from app.forms import *

def home(request):
    return render(request,'home.html')



def register(request):
    user_form=UserForm()
    profile_form=ProfileForm()
    return render(request,'register.html',context={'user_form':user_form,'profile_form':profile_form})