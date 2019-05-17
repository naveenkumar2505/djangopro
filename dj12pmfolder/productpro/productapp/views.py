from django.shortcuts import render
from .models import ProductData
from .forms import ProductForm
def home(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            pid=request.POST.get('pid','')
            pname=request.POST.get('pname','')
            cname=request.POST.get('cname','')
            cost=request.POST.get('cost','')
            color=request.POST.get('color','')
            weight=request.POST.get('weight','')
            mfgdate=form.cleaned_data.get('mfgdate','')
            data=ProductData(pid=pid,
                        pname=pname,
                        cname=cname,
                        color=color,
                        weight=weight,
                        cost=cost,
                        mfgdate=mfgdate)
            data.save()
            form=ProductForm()
            return render(request,'product.html',{'form':form})
    else:
        form=ProductForm()
        return render(request,'product.html',{'form':form})