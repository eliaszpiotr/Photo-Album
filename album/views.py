from django.shortcuts import render
from .models import Photo, Category


# Create your views here.
def album(request):
    photos = Photo.objects.all()
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
    return render(request, 'album/upload.html')
