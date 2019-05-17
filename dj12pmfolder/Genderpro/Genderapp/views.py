from django.shortcuts import render
def home(request):
    return render(request,'gender_home.html')
def boys(request):
    return render(request,'gender_boys.html')
def girls(request):
    return render(request,'gender_girl.html')

