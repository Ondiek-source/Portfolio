from django.contrib import admin
from .models import Drink

# Define the admin class
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name','description')

# Register the admin class with the associated model
admin.site.register(Drink, DrinkAdmin)

