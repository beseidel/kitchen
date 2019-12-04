
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Kitchen
from django.urls import reverse

import boto3


def login_required(function):
   def wrapper(*args, **kwargs):
      if args[1].session.get('user'):
         session = args[1].session.get('user')
         return function(*args, **kwargs)
      else:
         return HttpResponseRedirect(reverse('kitchen:login'))
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

def addToBucket(kitchen_name, file):
      filename = file.name
      fileExtension = '.' + filename.split(".")[1].lower()
      key = str(kitchen_name + fileExtension)

      session = boto3.session.Session(aws_access_key_id='AKIAJOXX6WYXL6SGEPDA', aws_secret_access_key='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')
      s3 = session.resource('s3')
      s3.Bucket('kitchenfeast').put_object(Key=key, Body=file, ACL='public-read')

      return key
      


