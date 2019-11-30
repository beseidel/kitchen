app_name='kitchen'

from django.urls import path, include
from django.conf.urls import url


from .viewsAuth import Index

from. viewsProvider import MenuView, KitchenView



urlpatterns = [
    #User Authentication
    path('', Index.as_view()),

    # Provider Path
    url(r'^kitchen/(?P<provider_key>.*)/$', KitchenView.as_view()), # Subject to change 
    url(r'^menu/(?P<kitchen_key>.*)/$', MenuView.as_view()), # Subject to change 
    

    # Buyer Path
    path('buyer/', Index.as_view()),    # Subject to change 


]
