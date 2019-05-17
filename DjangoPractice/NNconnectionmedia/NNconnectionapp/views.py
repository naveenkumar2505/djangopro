from django.shortcuts import render
from .models import Registration,Login
# Create your views here.

def home(request):
    return render(request,'basicPage.html')

def reg(request):
    if request.method=='POST':
        fname=request.POST.get('firstname','')
        lname=request.POST.get('lastname','')
        email=request.POST.get('email','')
        num=request.POST.get('num','')
        pas=request.POST.get('pas','')
        dob=request.POST.get('dob','')
        gen=request.POST.get('gen','')
        data=Registration(firstname=fname,surname=lname,email=email,
                     number=num,password=pas,dob=dob,gender=gen)
        data.save()
        return render(request,'homepage.html')
    return render(request,'homepage.html')

def login(request):
    if request.method=='post':
        login=request.POST.get('login')
        password=request.POST.get('password')
        data=Login(user=login,password=password)
        data.save()
        return render(request, 'login.html')
    return render(request,'login.html')

def lagout(request):
    pass

