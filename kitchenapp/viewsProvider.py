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

class AddKitchen(View):
   
   @login_required
   @seller_required
   def get(self, request):
      form = AddKitchenForm()
      return render(request, 'forms.html', {'form': form})


   @login_required
   @seller_required
   def post(self, request):
      form = AddKitchenForm(request.POST, request.FILES)
      if form.is_valid():
         kitchen_name = form.cleaned_data['kitchen_name']
         file = form.cleaned_data['image']
         image_url = 'https://kitchenfeast.s3.us-east-2.amazonaws.com/' + addToBucket(kitchen_name, file)

         kitchen_session = KitchenSession(request)
         Kitchen.objects.create(kitchen_name=kitchen_name, image_url=image_url, provider=kitchen_session.getUserObject())

         return HttpResponseRedirect(reverse('kitchen:providerKitchenView')) 

      return HttpResponseRedirect(reverse('kitchen:addKitchen')) 


class ProviderKitchenView(View):
   @login_required
   @seller_required
   def get(self, request):
      kitchen_session = KitchenSession(request)
      provider = kitchen_session.getUserObject()
      kitchens = Kitchen.objects.filter(provider=provider)
      return render(request, 'kitchen.html', {"kitchens":kitchens, 'provider': True})




class AddDish(View):
   def get(self, request, kitchen_id):
      kitchen_session = KitchenSession(request)
      dishes = Menu.objects.filter(kitchen=kitchen_session.getKitchenObject(kitchen_id))
      return render(request, 'menu.html', {'form': AddDishForm(), 'dishes':dishes, 'provider': kitchen_session.isProvider() })
   
   
   @login_required
   @seller_required
   def post(self, request, kitchen_id):
      form = AddDishForm(request.POST)
      if form.is_valid():
         dish_name, price, is_vegan = form.cleaned_data['dish_name'], form.cleaned_data['price'], form.cleaned_data['is_vegan']
         Menu.objects.create(dish_name=dish_name,price=price, is_vegan=is_vegan, kitchen=KitchenSession(request).getKitchenObject(kitchen_id) )
         
      
      return redirect('kitchen:addDish', kitchen_id=kitchen_id)

         

  







