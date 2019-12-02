from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
# models
from .models import User, Kitchen, WorkingDay, Menu

from .forms import SignUpForm, LoginForm, AddDishForm, AddKitchenForm


class Index(View):
   
   def get(self, request):
      form = AddKitchenForm()
      return render(request, 'forms.html', {'form':form})
      
   def post(self, request):
      #form = AddKitchenForm(request.POST, request.FILES)
      # print(request.FILES)
      # print(request.POST)
      
      # if form.is_valid():
      #    form.save()
      #    print(form.cleaned_data['name'])
      #    print(form.cleaned_data['image'])

      import boto3
      session = boto3.session.Session(aws_access_key_id='AKIAJOXX6WYXL6SGEPDA',
                                    aws_secret_access_key='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')
      s3 = session.resource('s3')
      s3.Bucket('kitchenfeast').put_object(Key='jusitn kke.jpg', Body=request.FILES.get('image'), ACL='public-read')
      
      
      
      return HttpResponse("Not added")

class Signup(View):
   def get(self, request):
      form = SignUpForm()
      return render(request, 'forms.html', {'form':form})
   
   def post(self, request):
      pass


class Login(View):

   def get(self, request):
      pass

   def post(self, request):
      pass




class Logout(View):
   def post(self, request):
      pass




