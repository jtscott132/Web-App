from django.urls import path
from . import views 

#URL Config Module
urlpatterns = [
    path('hello/', views.say_hello)
]