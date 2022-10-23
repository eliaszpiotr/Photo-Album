from django.shortcuts import render


# Create your views here.
def album(request):
    return render(request, 'album/album.html')


def photoView(request):
    return render(request, 'album/photo.html')


def photoUpload(request):
    return render(request, 'album/upload.html')
