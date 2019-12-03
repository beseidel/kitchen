from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
# models
from .models import User, Kitchen, WorkingDay, Menu, Cart
from .forms import SignUpForm, LoginForm, AddDishForm, AddKitchenForm
from .session import KitchenSession
from .authenticate import login_required, authenticate_user, seller_required, addToBucket
import boto3

from .serializer import DishSerialize



class AllKitchenView(View):
   
   def get(self, request):
      kitchens = Kitchen.objects.all()
      kitchen_session = KitchenSession(request)
      user = kitchen_session.is_login()
      provider = kitchen_session.isProvider()
      return render(request, 'buyer_kitchen.html', {'kitchens':kitchens, 'login': user[0], 'username':user[1], 'provider': provider  })

class CartView(ListView):
   
   @login_required
   def get(self, request):
      kitchen_session = KitchenSession(request)
      cart = Cart.objects.filter(user=KitchenSession(request).getUserObject() )
      user = kitchen_session.is_login()
      return render(request, 'cart.html', {'cart':cart, 'login':user[0], 'username': user[1]  })
      


class MenuView(View):

   def get(self, request, kitchen_id):
      kitchen_session = KitchenSession(request)
      kitchen = kitchen_session.getKitchenObject(kitchen_id)
      dishes = Menu.objects.filter(kitchen=kitchen)
      
      user = kitchen_session.is_login()
      return render(request, 'buyer_menu.html', {'dishes': dishes, 'kitchen_name':kitchen.kitchen_name, 'login': user[0], 'username':user[1] })
      

class AddToCart(APIView):
   @login_required
   def post(self, request):
      serializer = DishSerialize(data=request.data)
      if serializer.is_valid():
         form = serializer.data
         dish_id = form['dish_id']
         print(dish_id)
         kitchen_session = KitchenSession(request)
         Cart.objects.create(user=kitchen_session.getUserObject(), dish=kitchen_session.getDishObject(dish_id))
         return Response({'status': "OK"})
         
      return Response({'status': "error"})
