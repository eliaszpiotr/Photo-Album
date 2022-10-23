from django.shortcuts import render, redirect
from .models import Photo, Category


# Create your views here.
def album(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {
        'photos': photos,
        'categories': categories,
    }
    return render(request, 'album/album.html', context)


def photoView(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'album/photo.html', {'photo': photo})


def photoUpload(request):
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

        Photo.objects.create(category=category, description=data['description'], image=image)

        return redirect('album')

    return render(request, 'album/upload.html', {'categories': categories})
