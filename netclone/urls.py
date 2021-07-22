from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
urlpatterns= [
    path('clone/',views.clone, name='clone'),
    path('youtube/<str:id>',views.youtube,name = 'youtube'),
    path('search/',views.search_results, name ='search_results'),
    path('register/',views.register,name='register'),
    path('',views.home,name='home')
]
