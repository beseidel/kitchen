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

from .forms import UserForm, LoginForm


class Index(View):
   
   def get(self, request):
      form = LoginForm()
      return render(request, 'forms.html', {'form':form})
      
   def post(self, request):
      form = LoginForm(request.POST)      
      form.save()
      # form.setProviderTrue()
      print("OOKOOKOKOKOKOKOKO")

      return HttpResponse("mnoneaef")

class Signup(View):
   def get(self, request):
      pass

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




