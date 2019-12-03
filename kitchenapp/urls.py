from django.urls import path, include
from django.conf.urls import url

from .viewsAuth import Signup, Login, Logout
from .viewsProvider import AddKitchen, ProviderKitchenView, AddDish
from .viewsBuyer import AllKitchenView, MenuView, AddToCart, CartView

app_name='kitchen'

urlpatterns = [
    #User Authentication
    path('', AllKitchenView.as_view(), name='index'),
    url(r'^signup/$', Signup.as_view(), name='signup'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    
    # Provider Path   
    url(r'^addKitchen/$', AddKitchen.as_view(), name='addKitchen'), # Subject to change 
    url(r'^myKitchens/$', ProviderKitchenView.as_view(), name='providerKitchenView'), # Subject to change 
    url(r'^menu/kitchen/(?P<kitchen_id>.*)/$', AddDish.as_view(), name='addDish'), # Subject to change 
    
    
    # Buyer Path
    url(r'^view/menu/kitchen(?P<kitchen_id>.*)/$', MenuView.as_view(), name='viewMenu'), # Subject to change 
    url(r'^addToCart/$', AddToCart.as_view(), name='addToCart'), # Subject to change 
    url(r'^shoppingCart/$', CartView.as_view(), name='shoppingCart'), # Subject to change 

]



# url(r'^kitchen/(?P<provider_key>.*)/$', KitchenView.as_view()), # Subject to change 
# url(r'^menu/(?P<kitchen_key>.*)/$', MenuView.as_view()), # Subject to change 