from django.shortcuts import render
from .models import Registration
from .forms import Registration_Form
from django.contrib.auth import get_user_model
user=get_user_model()
def Reg_View(request):
    if request.method=='POST':
        form=Registration_Form(request.POST)
        if form.is_valid():
            first_name=request.POST.get('first_name','')
            second_name=request.POST.get('second_name','')
            email=request.POST.get('email','')
            password=request.POST.get('password','')

            data=Registration(first_name=first_name,
                         second_name=second_name,
                         email=email,password=password)
            data.save()
            form = Registration_Form()
            return render(request, 'registration.html', {'form': form})
    else:
        form=Registration_Form()
        return render(request,'registration.html',{'form':form})

