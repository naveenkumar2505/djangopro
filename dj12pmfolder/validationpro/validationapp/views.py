from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import RegistrationForm
from .models import RegstrationData
user=get_user_model()
def RegVal(request):
    form=RegistrationForm(request.POST or None )
    context={
        'form':form
    }
    if form.is_valid():
        first_name=form.cleaned_data.get('first_name')
        last_name=form.cleaned_data.get('last_name')
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        password2=form.cleaned_data.get('password2')
        new_user=user.objects.create_user(username,email,password)
        print(new_user)
        data=RegstrationData(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            password2=password2)
        data.save()
        return render(request,'validation.html',context)
    else:
        return render(request,'validation.html',context)



