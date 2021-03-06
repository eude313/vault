from django.shortcuts import render,redirect 
from .models import Category, Photo
# Create your views here.
def home(request):
    return render(request, 'phtos/home.html' )

def gallery(request):
    category=request.GET.get('category')
    if category == None:
        photo = Photo.objects.all()
    else:
        photo = Photo.objects.filter(category__name=category)
    
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES['image']
        
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
        return redirect('gallery') 
    context = {'categories': categories, 'photos': photo }
    return render(request, 'phtos/gallery.html', context )

def viewImage(request, pk):
    photos = Photo.objects.get(id=pk)
    if request.method == 'POST':
        photos.delete()
        return redirect('gallery')
    return render(request, 'phtos/photo.html', {'photo': photos})