from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
def home(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Data is inserted')
        else:
            return HttpResponse('Data is not inserted')
    else:
        form=ContactForm()
        return render(request,'Simplecontact.html',{'abc':form})