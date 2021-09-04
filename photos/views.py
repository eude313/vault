from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'phtos/home.html' )

def gallery(request):
    return render(request, 'phtos/gallery.html' )

def addImage(request):
    return render(request, 'phtos/add.html' )

def viewImage(request, pk):
    return render(request, 'phtos/photo.html' )