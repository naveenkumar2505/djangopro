from django.shortcuts import render
from .models import Employee,Login
from django.db.models import Q
from django.http import HttpResponseRedirect

def inserting(request):
    if request.method=='POST':
        id=request.POST.get('id')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        sal=request.POST.get('sal')
        email=request.POST.get('email')
        loc=request.POST.get('loc')
        com=request.POST.get('com')
        data=Employee(id=id,
                firstname=fname,
                 lastname=lname,
                 salary=sal,
                 email=email,
                 location=loc,
                 company=com)
        data.save()
        return render(request, 'inserting.html')
    return render(request,'inserting.html')

def search(request):
    if request.method=='POST':
        searchK=request.POST['searchKey']
        if searchK:
            match=Employee.objects.filter(Q(firstname__icontains=searchK)|
                                          Q(lastname__icontains=searchK))

            if match:
                return render(request,'search.html',{'match':match})
            else:
                from email import message
                message.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'search.html')

def update(request):
    if request.method=='POST':
        uid=request.POST.get['id']
        loc=request.POST.get['loc']
        sal=request.POST.get['sal']
        jid=Employee.objects.filter(id=uid)
        if jid:
            jid.update(location=loc)
            jid.update(salary=sal)
            return render(request,'update.html',{'mesg':'jid'})
        print('Data not found')

def delete(request):
    id=request.POST.get['id']
    id=Employee.objects.filter(id=id)
    if id:
        id.delete()
        return render(request,'delete.html',{'id':id})
    else:
        print('invalid Id')

def display(request):
    data=Employee.objects.all()
    return render(request,'display.html',{'data':data})
def login(request):
    if request.method=='POST':
        user=request.POST['user']
        password=request.POST['password']
        dob=request.POST['dob']

        data=Login(user=user,password=password,dob=dob)
        data.save()
        return render(request,'login.html')
    else:
        return render(request,'login.html')