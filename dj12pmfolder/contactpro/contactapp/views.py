from django.shortcuts import render
from .forms import ContactForm
from .models import ContactData
def home(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name1=request.POST.get('name','')
            company1=request.POST.get('company','')
            salary1=request.POST.get('salary','')
            mobile1=request.POST.get('mobile','')
            email1=request.POST.get('email','')
            username1=request.POST.get('username','')
            password1=request.POST.get('password','')
            data=ContactData(name=name1,
                             company=company1,
                             salary=salary1,
                             mobile=mobile1,
                             email=email1,
                             username=username1,
                             password=password1)
            data.save()
            form=ContactForm()
            return render(request,'contact.html',{'form':form})
    else:
        form=ContactForm()
        return render(request,'contact.html',{'form':form})