from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_user(request):
    data = request.POST.dict()
    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/articles/all/')
        else:
            return HttpResponse('Not active')
    else:
        return HttpResponse('Wrong username and password.')


@csrf_exempt
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/articles/all/')


@csrf_exempt
def register_user(request):
    data = request.POST.dict()
    try:
        user = User.objects.get(username=data['username'])
        return HttpResponse('WRONG')
    except(Exception):
        pass
    try:
        user = User.objects.get(email=data['email'])
        return HttpResponse('WRONG')
    except(Exception):
        pass
    user = User(username=data['username'],
                email=data['email'])
    user.set_password(data['password'])
    user.save()
    return login_user(request)