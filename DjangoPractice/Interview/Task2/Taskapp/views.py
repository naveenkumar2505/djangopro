from django.shortcuts import render
from .forms import ProductForm,OrderForm,OrderItemForm


def ProductView(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
    form=ProductForm()
    return render(request,'product.html',{'form':form})



def OrderView(request):
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
    form=OrderForm()
    return render(request,'Order.html',{'form':form})



def OrderItemView(request):
    if request.method=='POST':
        form=OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
    form=OrderItemForm()
    return render(request,'OrderItem.html',{'form':form})
