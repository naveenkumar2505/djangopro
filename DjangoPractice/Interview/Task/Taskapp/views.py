from django.shortcuts import render
from .models import Product
from .form import ProductForm,OrcerForm
from django.http.response import HttpResponse
def productView(request):
    if request.method=='post':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form=Product.objects.all()
            return render(request, 'product.html', {'form': form})
        return HttpResponse('data not found')
    else:
        form=ProductForm()
        return render(request,'product.html',{'form':form})

def orderView(request):
    if request.method=='POST':
        form=OrcerForm(request.POST)
        if form.is_valid():
            form.save()
        form=OrcerForm()
        return render(request,'order.html',{'form':form})
    else:
        form=OrcerForm()
        return render(request,'order.html',{'form':form})