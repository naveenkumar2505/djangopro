from django.shortcuts import render
from .forms import ConForm
from .models import ConData
def home(request):
    if request.method=='POST':
        form=ConForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name','')
            number=request.POST.get('number','')
            data=ConData(name=name,
                         number=number)
            data.save()
            form=ConForm()
            return render(request,'con1.html',{'form':form})
    else:
        form=ConForm()
        return render(request,'con1.html',{'form':form})