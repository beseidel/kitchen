from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
# models
from .models import Provider, Buyer, Kitchen, WorkingDay, Menu



class Index(View):
   def get(self, request):
      return HttpResponse("Added")

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




