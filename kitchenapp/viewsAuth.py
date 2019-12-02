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
from .session import Session
from .authenticate import login_required, authenticate_user
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
      
      form = SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         
      return HttpResponse('Successfully Signed Up')



class Login(View):

   def get(self, request):
      form = LoginForm()
      return render(request, 'forms.html', {'form': form})

   def post(self, request):
      form = LoginForm(request.POST)

      if form.is_valid():
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         if authenticate_user(request, username, password):
            print('======> ' ,authenticate_user(request, username, password))
            return HttpResponse('Logged in')
         

      return HttpResponseRedirect(reverse('kitchen:login'))



class Logout(View):
   def post(self, request):
      pass




