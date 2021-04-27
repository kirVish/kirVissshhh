from django.conf.urls import *
from django.urls import path, include
from . import views


app_name = 'pets'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pet_id>/', views.PetDetail.as_view(), name = 'detail')
]
