from django.contrib import admin
from .models import User, Kitchen, Menu, WorkingDay, KitchenImage

# Register your models here.

admin.site.register(User)
admin.site.register(Kitchen)
admin.site.register(KitchenImage)
admin.site.register(Menu)
admin.site.register(WorkingDay)