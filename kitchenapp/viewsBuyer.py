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
from .session import KitchenSession
from .authenticate import login_required, authenticate_user, seller_required, addToBucket
import boto3



class AllKitchenView(ListView):
   queryset = Kitchen.objects.all()
   context_object_name='kitchens'
   template_name='kitchen.html'



class MenuView(View):

   def get(self, request, kitchen_id):
      dishes = Menu.objects.filter(kitchen=KitchenSession(request).getKitchenObject(kitchen_id))
      return render(request, 'menu.html', {'dishes': dishes, 'provider': False})
      


