from django.http import HttpResponse
def horror(request):
    x='Horror Movies'
    return HttpResponse(x)
def warrior(request):
    x='warrior Movies'
    return HttpResponse(x)

