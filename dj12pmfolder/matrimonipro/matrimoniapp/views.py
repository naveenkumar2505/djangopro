from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm,LoginForm,PasswordForm
from .models import RegistrationData
def registration(request):
    if request.method=='POST':
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            firstname=request.POST.get('firstname','')
            lastname=request.POST.get('lastname','')
            username=request.POST.get('username','')
            password1=request.POST.get('password1','')
            password2=request.POST.get('password2','')
            email=request.POST.get('email','')
            mobile=request.POST.get('mobile','')
            dob=request.POST.get('dob','')
            gender=request.POST.get('gender','')
            job=request.POST.get('job','')
            salary=request.POST.get('salary','')
            height=request.POST.get('height','')
            weight=request.POST.get('weight','')
            color=request.POST.get('color','')
            loc=request.POST.get('loc','')
            data=RegistrationData(firstname=firstname,lastname=lastname,username=username,
                                  password1=password1,password2=password2,email=email,mobile=mobile,
                                  dob=dob,height=height,weight=weight,color=color,salary=salary
                                  ,job=job,loc=loc,gender=gender
                                  )
            data.save()
        return redirect('/login/')
    else:
        rform=RegistrationForm()
        return render(request,'registration.html',{'rform':rform})
def login(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username','')
            password1=request.POST.get('password1','')
            user=RegistrationData.objects.filter(username=username)
            password=RegistrationData.objects.filter(password1=password1)
            print(user)
            print(password)
            if  user and password:
                return HttpResponse('user does not exists')
            else:
                return redirect('/home/')
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})
def home(request):
    return render(request,'home.html')
def girls(request):
    data=RegistrationData.objects.filter(gender='female')
    return render(request,'girls.html',{'data':data})
def boys(request):
    data=RegistrationData.objects.filter(gender='male')
    return render(request,'boys.html',{'data':data})
def clients(request):
    return render(request,'clients.html')
def forgetpass(request):
    if request.method=='POST':
        pform=PasswordForm(request.POST)
        if pform.is_valid():
            username=pform.cleaned_data['username']
            pass1=pform.cleaned_data['password1']
            pass2=pform.cleaned_data['password2']
            user = RegistrationData.objects.filter(username=username)
            if pass1==pass2:
                    user.update(password1=pass1)
                    user.update(password2=pass2)
                    return redirect('/login/')
            else:
                return HttpResponse('User Does not Exists')
    else:
        pform=PasswordForm()
        return render(request,'forgot.html',{'pform':pform})
def multi(request):
    if request.method=='POST':
        if request.POST.get('submit')=='signin':
            #login code
            if request.method == 'POST':
                if request.method == 'POST':
                    lform = LoginForm(request.POST)
                    if lform.is_valid():
                        username = request.POST.get('username', '')
                        password1 = request.POST.get('password1', '')
                        user = RegistrationData.objects.filter(username=username)
                        password = RegistrationData.objects.filter(password1=password1)
                        print(user)
                        print(password)
                        if user and password:
                            return HttpResponse('user does not exists')
                        else:
                            return redirect('/home/')
                else:
                    lform = LoginForm()
                    return render(request, 'login.html', {'lform': lform})


            else:
                lform = LoginForm()
                return render(request, 'multi.html', {'lform': lform})
        elif request.POST.get('submit')=='signup':
            #Registration code
            if request.method == 'POST':
                rform = RegistrationForm(request.POST)
                if rform.is_valid():
                    firstname = request.POST.get('firstname', '')
                    lastname = request.POST.get('lastname', '')
                    username = request.POST.get('username', '')
                    password1 = request.POST.get('password1', '')
                    password2 = request.POST.get('password2', '')
                    email = request.POST.get('email', '')
                    mobile = request.POST.get('mobile', '')
                    dob = request.POST.get('dob', '')
                    gender = request.POST.get('gender', '')
                    job = request.POST.get('job', '')
                    salary = request.POST.get('salary', '')
                    height = request.POST.get('height', '')
                    weight = request.POST.get('weight', '')
                    color = request.POST.get('color', '')
                    loc = request.POST.get('loc', '')
                    data = RegistrationData(firstname=firstname, lastname=lastname, username=username,
                                            password1=password1, password2=password2, email=email, mobile=mobile,
                                            dob=dob, height=height, weight=weight, color=color, salary=salary
                                            , job=job, loc=loc, gender=gender
                                            )
                    data.save()
                return redirect('/multi/')
    else:
        lform=LoginForm()
        rform=RegistrationForm()
        return render(request,'multi.html',{'lform':lform,'rform':rform})