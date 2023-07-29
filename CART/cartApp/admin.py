from django.contrib import admin
from cartApp.models import Product
# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display=['Item','product','price','quantity']
admin.site.register(Product,productAdmin)    
