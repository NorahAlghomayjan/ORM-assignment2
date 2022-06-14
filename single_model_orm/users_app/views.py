from django.shortcuts import render , redirect
from .models import Users

# Create your views here.

def index(request):

    context = {
        'all_users' :Users.objects.all()
    }

    return render(request,'addUser.html',context)

def addUser (request):
    if not(request.method == 'POST'):
        return redirect('/')
    
    first_Name = request.POST.get('first_name')
    last_Name = request.POST.get('last_name')
    email = request.POST.get('email')
    age = request.POST.get('age')

    Users.objects.create(first_name=first_Name,last_name=last_Name,email_address=email,age=age)

    return redirect('/')