from django.shortcuts import render
from .models import Drop
from .forms import MyModelForm
def dropview(request):
    if(request.method=='POST'):
        form=MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            form=MyModelForm()
            return render(request,'drop.html',{'form':form})
    form = MyModelForm()
    return render(request,'drop.html',{'form':form})
