from django.urls import path, include
from django.conf.urls import url

from .viewsAuth import Signup, Login, Logout
from .viewsProvider import AddKitchen, ProviderKitchenView
from .viewsBuyer import AllKitchenView, MenuView

app_name='kitchen'

urlpatterns = [
    #User Authentication
    path('', AllKitchenView.as_view(), name='index'),
    url(r'^signup/$', Signup.as_view(), name='signup'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    
    # Provider Path   
    url(r'^addKitchen/$', AddKitchen.as_view(), name='addKitchen'), # Subject to change 
    url(r'^providerKitchenView/$', ProviderKitchenView.as_view(), name='providerKitchenView'), # Subject to change 
    url(r'^menu/kitchen/(?P<kitchen_id>.*)/$', AddKitchen.as_view(), name='addKitchen'), # Subject to change 
    
    
    # Buyer Path
    # path('buyer/', Index.as_view()),    # Subject to change 


]



# url(r'^kitchen/(?P<provider_key>.*)/$', KitchenView.as_view()), # Subject to change 
# url(r'^menu/(?P<kitchen_key>.*)/$', MenuView.as_view()), # Subject to change 