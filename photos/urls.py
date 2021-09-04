
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewImage, name='photo'),
    path('add/', views.addImage, name='addImage'),
    
]
