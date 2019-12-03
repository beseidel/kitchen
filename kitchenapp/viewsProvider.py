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

         userObj = request.session.get('user')
         provider = User.objects.get(username=userObj[0], password=userObj[1])
         Kitchen.objects.create(kitchen_name=kitchen_name, image_url=image_url, provider=provider)

         return HttpResponse('Added')

      return HttpResponse('Not Added')







class ProviderKitchenView(View):
   @login_required
   @seller_required
   def get(self, request):
      kitchen_session = KitchenSession(request)
      provider = kitchen_session.getUserObject()
      kitchens = Kitchen.objects.filter(provider=provider)
      return render(request, 'kitchen.html', {"kitchens":kitchens})



# class KitchenView(View):
#    def get(self, request, provider_key):
#       print('-------------------' , provider_key )
#       provider = Provider.objects.all() #
#       Kitchen.objects.filter()







