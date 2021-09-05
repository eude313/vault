from django.shortcuts import render
from .models import Category, Photo
# Create your views here.
def home(request):
    return render(request, 'phtos/home.html' )

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'phtos/gallery.html', context )

def addImage(request):
    return render(request, 'phtos/add.html' )

def viewImage(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request, 'phtos/photo.html', {'photo': photos})