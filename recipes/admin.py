from django.contrib import admin
from .models import Recipe, Tags, Comments

# Register your models here.
admin.site.register(Recipe)  # registering the app in the admin block 
admin.site.register(Comments) 
admin.site.register(Tags) 