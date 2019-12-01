from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
# models
from .models import User,  Kitchen, WorkingDay, Menu



# class GetKitchen(ListView):
#    # model = Kitchen
#    queryset = Kitchen.objects.all() # Get kitchen by provider
#    context_object_name='kitchenList'
# 	template_name='kitchenList.html'




class MenuView(View):
   def get(self, request, kitchen_key):
      print('-------------------' , kitchen_key )



class KitchenView(View):
   def get(self, request, provider_key):
      print('-------------------' , kitchen_key )


# class KitchenView(View):
#    def get(self, request, provider_key):
#       print('-------------------' , provider_key )
#       provider = Provider.objects.all() #
#       Kitchen.objects.filter()







