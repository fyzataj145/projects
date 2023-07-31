from django.contrib import admin
from petsApp.models import Pet
# Register your models here.
class petAdmin(admin.ModelAdmin):
    list_display=['id','name','gender','species','age','breed','description','image','price']
admin.site.register(Pet,petAdmin)    