
from django.urls import path, include
from . import views
urlpatterns = [
    path('index', views.index, name="index"),
    path('register', views.register_page, name="register_page"),
    path('register_path', views.register, name="register"),
    path('login_page', views.login_page, name='login_page'),
    path('logout_page', views.login_page, name='logout_page'),
]
