from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from .forms import RegistrationForm
from .models import RegstrationData
def RegVal(request):
    form=RegistrationForm(request.POST or None )
    context={
        'form':form
    }
    if form.is_valid():
        first_name=form.cleaned_data.get('first_name')
        second_name=form.cleaned_data.get('second_name')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        data=RegstrationData(
            first_name=first_name,
            second_name=second_name,
            email=email,
            password=password,
            )
        data.save()
        return render(request,'validation.html',context)
    else:
        return render(request,'validation.html',context)



