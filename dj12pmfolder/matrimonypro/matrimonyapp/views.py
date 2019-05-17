from django.shortcuts import render, redirect
from django.http import HttpResponse
from matrimonyapp.forms import RegistrationForm
from matrimonyapp.models import Register
from .forms import LoginForm

def home(request):
    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            fname = request.POST.get('fname', '')
            mname = request.POST.get('mname', '')
            mobile = request.POST.get('number', '')
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            email = request.POST.get('email', '')
            gender = request.POST.get('gender', '')
            age = request.POST.get('age', '')
            weight = request.POST.get('weight', '')
            # image = request.POST.get('image','')

            name = str(name)
            name = name.title()

            fname = str(fname)
            fname = fname.title()

            mname = str(mname)
            mname = mname.title()

            data = Register(name=name,
                            fname =fname,
                            mname= mname,
                            mobile=mobile,
                            email=email,
                            username=username,
                            password=password,
                            age=age,
                            gender=gender,
                            weight=weight,
                            # phote=image
                            )
            data.save()
            form = RegistrationForm()
            return render(request, 'matrimonyapp/register.html', {'form': form})
            # return HttpResponse("Data successfully inserted")
    else:
        form = RegistrationForm()
        return render(request, 'matrimonyapp/register.html', {'form': form})

    return render(request,'matrimonyapp/register.html')






def thankyou(request):
    return render(request,'matrimonyapp/thankyou.html')


def insert(request):
    return render(request,'insert.html')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username2 = request.POST.get('username', '')
            password2 = request.POST.get('password', '')
            dbuser = Register.objects.filter(username = username2 , password = password2)
            if dbuser:
                return redirect('/home')
            else:
                return redirect('/#/')
    else:
        form = LoginForm()
        return render(request, 'matrimonyapp/matrihome.html', {"form":form})
        # return render(request, "martrihome.html", {"form":form})


def girls_view(request):
    x = Register.objects.filter(gender='female')
    return render(request,'girls.html',{'girl':x})


def boys_view(request):
    y = Register.objects.filter(gender='male')
    return render(request,'boys.html',{'boy':y})


def searchage_view(request,a,g):
    s = Register.objects.filter(age=a, gender=g)
    return render(request,'girls.html',{'age':s})
