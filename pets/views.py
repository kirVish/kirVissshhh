from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *

# Create your views here.
class IndexView(View):
    def get(self, request):
        a = Pet.objects.all()
        context = {'a':a}
        return render(request, 'pets/index.html',context)
class PetDetail(DetailView):
    def get(self, request, pet_id):
        pet = get_object_or_404(Pet, pk = pet_id)
        return render(request, 'pets/detail.html',{'pet':pet})
   
    
   

    
