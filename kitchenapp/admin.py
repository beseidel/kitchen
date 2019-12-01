from django.contrib import admin
from .models import User, Kitchen, Menu, WorkingDay

# Register your models here.

admin.site.register(User)
admin.site.register(Kitchen)
admin.site.register(Menu)
admin.site.register(WorkingDay)