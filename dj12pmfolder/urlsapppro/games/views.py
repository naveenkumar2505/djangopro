from django.shortcuts import render
from django.http.response import HttpResponse
def cricket(request):
    x='It is international game'
    return HttpResponse(x)
def hockey(request):
    x='It is National Game'
    return HttpResponse(x)
