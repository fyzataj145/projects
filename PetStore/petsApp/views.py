from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from petsApp.models import Pet
# Create your views here.
class PetListView(ListView):
    queryset=Pet.objects.all()
    model=Pet
    template_name="petsApp/list.html"
    context_object_name = 'pet'

class PetDetailView(DetailView):
    queryset=Pet.objects.all()
    model=Pet
    template_name="petsApp/detail.html"
    def get_context_data(self, *args, **kwargs):
        context=super(PetDetailView,self).get_context_data(*args, **kwargs)
        return context   