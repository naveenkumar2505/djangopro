from django.shortcuts import render
from .models import RegistrationData

def reg(request):
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            user_name = request.POST.get('user_name')
            mobile_number = request.POST.get('mobile_number')
            email = request.POST.get('email')
            data = RegistrationData(first_name=first_name, last_name=last_name,
                                    user_name=user_name, mobile_number=mobile_number, email=email)
            data.save()
            return render(request, 'reg.html')
        else:
            return render(request, 'reg.html')
def hello(request):
    return render(request,'hello.html')