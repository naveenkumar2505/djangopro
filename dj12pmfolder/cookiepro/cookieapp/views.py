from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h4>cookie was first by a programmer"
                        "named louis moatuall in 1994<br>"
                        "at Netscap communications"
                        "in their Netscape browser</h4>")
def test_cookie(request):
    if not request.COOKIES.get('color'):
        response=HttpResponse('cookie set')
        response.set_cookie('color','blue')
        return response
    else:
        return HttpResponse("your favorite"
                            "color is{0}".format(request.COOKIES['color']))
def count_cookie(request):
    if not request.COOKIES.get('visits'):
        response=HttpResponse("this is your favorite visit to the site"
                     "from now on i will try "
                     "your visits to this site")
        response.set_cookie('visits','1')
        return response
    else:
        visits=int(request.COOKIES.get('visits'))+1
        response=HttpResponse("this is your {0} visit".format(visits))
        response.set_cookie('visits',str(visits))
        return response
def delete_cookie(request):
    if request.COOKIES.get('visits'):
        response=HttpResponse("cookies cleared")
        response.delete_cookie('visits')
        return response
    else:
        response=HttpResponse("we are not tracking you")
        return response