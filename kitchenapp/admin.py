from django.contrib import admin
from .models import Provider, Buyer, Kitchen, Menu, WorkingDay

# Register your models here.

admin.site.register(Provider)
admin.site.register(Buyer)
admin.site.register(Kitchen)
admin.site.register(Menu)
admin.site.register(WorkingDay)