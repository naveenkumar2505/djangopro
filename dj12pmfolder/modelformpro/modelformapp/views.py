from django.shortcuts import render
from .forms import ModelFormF

def modelView(request):
    form=ModelFormF(request.POST)
    if form.is_valid():
        form.save()
        form=ModelFormF()
        return render(request,'model.html',{'form':form})
    else:
        form = ModelFormF()
        return render(request, 'model.html', {'form': form})