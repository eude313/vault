from django.shortcuts import render
from .models import Category, Photo
# Create your views here.
def home(request):
    return render(request, 'phtos/home.html' )

def gallery(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None  
            
    photo = Photo.objects.create(
        category=category,
        description = data['description'],
        image=image,
    )        
            
    photo = Photo.objects.all()
    context = {'categories': categories, 'photos': photo }
    return render(request, 'phtos/gallery.html', context )

def addImage(request):
    return render(request, 'phtos/add.html' )

def viewImage(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request, 'phtos/photo.html', {'photo': photos})