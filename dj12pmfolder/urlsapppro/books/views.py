from django.shortcuts import render
from django.http import HttpResponse
def bb1(request):
    x='good book'
    return HttpResponse(x)
def bb2(request):
    x='best book in world'
    return HttpResponse(x)
