from django.urls import path
from .views import album, photoView, photoUpload

urlpatterns = [
    path('', album, name='album'),
    path('photo/<str:pk>', photoView, name='photo'),
    path('upload/', photoUpload, name='upload'),
]