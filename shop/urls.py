from django.contrib import admin
from django.urls import path , include
from .views import index

app_name="shop"
urlpatterns = [
   path("index/" , index , name="index")
]