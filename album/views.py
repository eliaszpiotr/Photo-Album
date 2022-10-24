from django.shortcuts import render, redirect
from .models import Photo, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('album')

    return render(request, 'album/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('album')

    context = {'form': form, 'page': page}
    return render(request, 'album/login_register.html', context)


@login_required(login_url='login')
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

@login_required(login_url='login')
def photoView(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'album/photo.html', {'photo': photo})

@login_required(login_url='login')
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