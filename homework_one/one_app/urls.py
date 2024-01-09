from .views import index, about_me
from django.urls import path


urlpatterns = [

    path('index', index, name='index'),

    path('about_me', about_me, name='about_me'),

]
