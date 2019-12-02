from django.urls import path, include
from django.conf.urls import url

from .viewsAuth import Index, Signup, Login, Logout
from .viewsProvider import MenuView, KitchenView
from .viewsBuyer import *

app_name='kitchen'
app_name='kitchen'
urlpatterns = [
    #User Authentication
    path('', Index.as_view()),
    url(r'^signup/$', Signup.as_view(), name='signup'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    
    # Provider Path
    url(r'^kitchen/(?P<provider_key>.*)/$', KitchenView.as_view()), # Subject to change 
    url(r'^menu/(?P<kitchen_key>.*)/$', MenuView.as_view()), # Subject to change 
    

    # Buyer Path
    path('buyer/', Index.as_view()),    # Subject to change 


]
