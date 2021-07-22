from django.shortcuts import render
import requests,json
import os
from decouple import config
from googleapiclient.discovery import build
from .form import UserRegisterForm
from django.contrib import messages

# Create your views here.

def netflix (request,category):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=da722b948a6bfa00f72d44ea5772cfe4'
    key = 'da722b948a6bfa00f72d44ea5772cfe4'
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=da722b948a6bfa00f72d44ea5772cfe4'
    url1 = url.format(category,key)
    url2 = requests.get(url1)
    url3 = url2.json()
    return url3

def clone (request):
    popular = netflix(request, 'popular')
    upcoming = netflix(request, 'upcoming')
    airingToday = netflix(request, 'airing_today')
    trending = netflix(request, 'trending')
    return render (request, 'index.html', {'popular': popular, 'upcoming': upcoming, 'airing_today': airingToday, 'trending': trending})


def youtube(request,id):
    youTubeKey =  config('youTubeKey')
    popular = home1(request,'popular')
    pp = ''
    for p in popular['results']:
        if str(p['id'])==str(id):
            pp = p['title']
    youtube = build('youtube','v3',developerKey = youTubeKey)
    request = youtube.search().list(q= pp+'trailer',part = 'snippet',type= 'video')
    res = request.execute()
    return render(request,'youtube.html',{'response':res})

def search_results(request):

    if 'movie' in request.GET and request.GET["movie"]:
        search_term = request.GET.get("movie")
        searched_movies = Movie.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"movies": searched_movies})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    

def home(request):
        # if request.user.is_authenticated:
            # return redirect(to='/profile/')
        return render(request,'user/home.html')
    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data['username']
            messages.success(request,f'Successfully created for {username}! Please login to continue')
            
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form})