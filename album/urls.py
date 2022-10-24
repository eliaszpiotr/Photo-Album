from django.urls import path
from .views import album, photoView, photoUpload, logoutUser, loginUser, registerUser

urlpatterns = [
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerUser, name="register"),
    path('', album, name='album'),
    path('photo/<str:pk>', photoView, name='photo'),
    path('upload/', photoUpload, name='upload'),
]
