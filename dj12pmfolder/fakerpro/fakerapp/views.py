from django.shortcuts import render,redirect
from .models import EmployeeData
from faker import Faker
fake=Faker()
def inserting(request):
    for i in range(100):
        first_name=fake.first_name()
        last_name=fake.last_name()
        email=fake.email()
        salary=fake.random_element(elements=(10000,20000,30000,40000))
        role=fake.random_element(elements=('GPM','PM','MGR','TL'))
        dob=fake.date()
        data=EmployeeData.objects.get_or_create(first_name=first_name,
                                           last_name=last_name,
                                           email=email,
                                           salary=salary,
                                           role=role,
                                           dob=dob)
        return redirect('/home/')
def fetching(request):
    data=EmployeeData.objects.all()
    return render(request,'faker.html',{'data':data})