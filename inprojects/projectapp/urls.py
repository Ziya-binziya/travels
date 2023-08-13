
from django.urls import path, include

from projectapp import views

urlpatterns = [
    path('',views.demo,name='demo')
]