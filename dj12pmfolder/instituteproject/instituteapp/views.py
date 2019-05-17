from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm,StudentForm,FeedbackForm,PasswordForm
from .models import RegistrationData,StudentData,FeedbackData
from django.http.response import HttpResponse
import datetime as d
time1=d.datetime.now()
def registrationview(request):
    if request.method=='POST':
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            First_Name=request.POST.get('First_Name','')
            Last_Name=request.POST.get('Last_Name','')
            User_Name=request.POST.get('User_Name','')
            Password1=request.POST.get('Password1','')
            Password2=request.POST.get('Password2','')
            Email=request.POST.get('Email','')
            Mobile=request.POST.get('Mobile','')
            dob=rform.cleaned_data.get('dob','')
            data=RegistrationData(
                First_Name=First_Name,
                Last_Name=Last_Name,
                User_Name=User_Name,
                Password1=Password1,
                Password2=Password2,
                Email=Email,
                Mobile=Mobile,
                dob=dob
            )
            data.save()
            return redirect('/#/')
            # rform=RegistrationForm()
            # return render(request,'registration.html',{'rform': rform})
    else:
            rform = RegistrationForm()
            return render(request, 'registration.html', {'rform': rform})
def lginview(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            UserName=request.POST.get('User_Name','')
            Password1=request.POST.get('Password1','')
            user=RegistrationData.objects.filter(User_Name=UserName)
            password=RegistrationData.objects.filter(Password1=Password1)
            if user and password:
                 return HttpResponse('Valid details')
            else:
                return redirect('/home/')

    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})
def home(request):
    return render(request,'inst_home.html')
def services(request):
    return render(request,'inst_services.html')
def contact(request):
    if request.method=='POST':
        sform=StudentForm(request.POST)
        if sform.is_valid():
            # if we have multiple data go for cleaned_data()
            Name=sform.cleaned_data.get('Name','')
            Mobile=sform.cleaned_data.get('Mobile','')
            Email=sform.cleaned_data.get('Email','')
            cources=sform.cleaned_data.get('cources','')
            trainer=sform.cleaned_data.get('trainer','')
            timing=sform.cleaned_data.get('timing','')
            startdate=sform.cleaned_data.get('startdate','')
            data=StudentData(Name=Name,Mobile=Mobile,Email=Email,
                cources=cources,trainer=trainer,timing=timing,startdate=startdate
            )
            data.save()
            sform = StudentForm()
            return render(request, 'contact.html', {'sform': sform})
    else:
        sform = StudentForm()
        return render(request, 'contact.html', {'sform': sform})
def feedback(request):
    if request.method=='POST':
         fform=FeedbackForm(request.POST)
         if fform.is_valid():
             name=request.POST.get('name','')
             rating=request.POST.get('rating','')
             feedback=request.POST.get('feedback','')
             name=name.title()
             data=FeedbackData(
                 name=name,
                 rating=rating,
                 time=time1,
                 feedback=feedback
             )
             data.save()
             return redirect('/feedback/')

    else :
        fdata=FeedbackData.objects.all()
        fform=FeedbackForm()
        return render(request,'feedback.html',{'fform':fform,'fdata':fdata})
def gallery(request):
    return render(request,'gallery.html')

def forgetpass(request):

    if request.method=="GET":
        pform=PasswordForm()
        return render(request,'password.html',{'form':pform})
    else:
        pform=PasswordForm(request.POST)

        if pform.is_valid():

            user=pform.cleaned_data['User_Name']
            psw1=pform.cleaned_data['Password1']
            psw2=pform.cleaned_data['Password2']


            x=RegistrationData.objects.filter(User_Name=user)
            if psw1==psw2 and x:
                    x.update(Password1=psw1)
                    x.update(Password2=psw2)
                    return redirect('/#/')
                # pform=PasswordForm()
                # return render(request,'password.html',{'pform':pform})
            else:
                return HttpResponse('User does not exist')

        else:

            return HttpResponse('Invalid Form')