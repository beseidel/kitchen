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



class AllKitchenView(ListView):
   queryset = Kitchen.objects.all()
   context_object_name='kitchens'
   template_name='buyer_kitchen.html'


class CartView(ListView):
   
   @login_required
   def get(self, request):
      kitchen_session = KitchenSession(request)
      cart = Cart.objects.filter(user=KitchenSession(request).getUserObject() )
      return render(request, 'cart.html', {'cart':cart})
      


class MenuView(View):

   def get(self, request, kitchen_id):
      kitchen = KitchenSession(request).getKitchenObject(kitchen_id)
      dishes = Menu.objects.filter(kitchen=kitchen)
      return render(request, 'buyer_menu.html', {'dishes': dishes, 'provider': False, 'kitchen_name':kitchen.kitchen_name })
      

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
