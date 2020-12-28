


import re
from django.contrib import admin
from djView import views
from django.urls import path,include


urlpatterns = [
    path('index/', views.index),

]