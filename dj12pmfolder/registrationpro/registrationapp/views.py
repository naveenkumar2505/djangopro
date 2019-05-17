from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
from .models import RegistrationData
from django.http import HttpResponse
def regview(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=request.POST.get('first_name','')
            last_name=request.POST.get('last_name','')
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            mobile=request.POST.get('mobile','')
            email=request.POST.get('email','')
            gender=request.POST.get('gender','')
            data=RegistrationData(first_name=first_name,
                             last_name=last_name,
                             username=username,
                             password=password,
                             mobile=mobile,
                             email=email,
                             gender=gender)
            data.save()
            form=RegistrationForm()
            return render(request,'registration.html',{'form':form})
    else:
        form=RegistrationForm()
        return render(request,'registration.html',{'form':form})
def logview(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            use1=RegistrationData.objects.filter(username=username)
            pwd1=RegistrationData.objects.filter(password=password)
            if  use1 and pwd1:
                return HttpResponse('Valid Data')
            else:
                return HttpResponse('InValid Data')
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})