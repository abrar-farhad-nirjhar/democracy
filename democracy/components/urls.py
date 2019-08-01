
from django.urls import path, include
from . import views
urlpatterns = [
    path('index', views.index, name="index"),
    path('register', views.register_page, name="register_page"),
    path('register_path', views.register, name="register")
]
