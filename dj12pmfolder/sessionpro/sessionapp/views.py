from django.shortcuts import render
from django.http import HttpResponse
def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse('cookie is set in the server')
def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response=HttpResponse('cookie test passed')
    else:
        response=HttpResponse('cookie failed')
    return response
def save_session_data(request):
    request.session['Eno']=1001
    request.session['Ename']='Naveen'
    request.session['Language']='python'
    request.session['Framework']='Django'
    return HttpResponse('session data saved')
def access_session_data(request):
    response=''
    if request.session.get('Eno'):
        response+='Eno:{}<br>'.format(request.session.get('Eno'))
    if request.session.get('Ename'):
        response+='Ename:{}<br>'.format(request.session.get('Ename'))
    if request.session.get('Language'):
        response+='Lanuage:{}<br>'.format(request.session.get('Language'))
    if request.session.get('Framework'):
        response+= 'Framework:{}<br>'.format(request.session.get('Framework'))
    if not response:
        return HttpResponse('No session data')
    else:
        return HttpResponse(response)
def delete_session(request):
   try:
       del request.session['Eno']
       del request.session['Ename']
       del request.session['Language']
       del request.session['Framework']
   except KeyError:
       print('key not found')
   return HttpResponse('session data cleared')