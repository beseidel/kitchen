
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.urls import reverse


def login_required(function):
   def wrapper(*args, **kwargs):
      if args[1].session.get('user'):
         session = args[1].session.get('user')
         print("===================>  ", session[2])
         return function(*args, **kwargs)
      else:
         return HttpResponse("Please log in.")
   return wrapper


def seller_required(function):
   def wrapper(*args, **kwargs):
      session = args[1].session.get('user')[2]
      if args[1].session.get('user')[2] == True:
         return function(*args, **kwargs)
      else:
         return HttpResponse("You are not a seller")
   return wrapper


def authenticate_user(request, username, password):
   userObj = User.objects.get(username=username, password=password)
   if userObj:
      request.session['user'] = (username, password, userObj.is_provider)
      return True
   return False



