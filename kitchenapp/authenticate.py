
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.urls import reverse


def login_required(function):
   def wrapper(*args, **kwargs):
      if args[1].session.get('user'):
         return function(*args, **kwargs)
      else:
         return HttpResponse("Not logged in")
   return wrapper


def authenticate_user(request, username, password):
   userObj = User.objects.filter(username=username, password=password)
   if userObj:
      request.session['user'] = (username, password)
      return True
   return False

