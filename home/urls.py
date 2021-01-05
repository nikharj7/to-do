
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    
]
