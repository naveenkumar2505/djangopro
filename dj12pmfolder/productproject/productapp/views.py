from django.shortcuts import render
from .forms import ProductModelForm,UpdateForm,deleteForm
from .models import Product
from django.http.response import HttpResponse

def home(request):
    return render(request,'home.html')

def insert(request):
    if request.method=='POST':
        form=ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductModelForm()
            return render(request, 'insert.html', {'form': form})
    else:
        form=ProductModelForm()
        return render(request, 'insert.html',{'form':form})

def update(request):
    if request.method=='POST':
        form=UpdateForm(request.POST)
        if form.is_valid():
            pid=form.cleaned_data['product_id']
            pcost=form.cleaned_data['product_cost']
            pcolor=form.cleaned_data['product_color']
            id=Product.objects.filter(product_id=pid)
            if id:
                id.update(product_cost=pcost)
                id.update(product_color=pcolor)
                return HttpResponse('data updated successfully')
            else:
                return HttpResponse('Invalid prouductId')
        else:
            return HttpResponse('please provide details')
    else:
        form=UpdateForm()
        return render(request,'update.html',{'form':form})

def delete(request):
    if request.method=='POST':
      form=deleteForm(request.POST)
      if form.is_valid():
          pid=form.cleaned_data['product_id']
          id=Product.objects.filter(product_id=pid)
          if id:
              id.delete()
              return HttpResponse('deleted record successfully....')
          else:
              return HttpResponse('Invalid Id')
      else:
          return HttpResponse('shoud provide id')
    else:
        form =deleteForm()
        return render(request,'delete.html',{'form':form})

def display(request):
    form=Product.objects.all()
    return render(request,'display.html',{'form':form})
