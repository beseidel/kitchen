app_name='kitchen'

from django.urls import path, include
from .viewsAuth import Index


urlpatterns = [
    #User Authentication
    path('', Index.as_view()),

    # Provider Path
    path('provider/', Index.as_view()), # Subject to change 


    # Buyer Path
    path('buyer/', Index.as_view()),    # Subject to change 
    



]
