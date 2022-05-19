from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
import json
import requests

def home(request):

    if request.method == 'POST':
        indeks = request.POST['indeks']
        api_request = requests.get(f"https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{indeks}")
        api_request2 = requests.get("https://api.gios.gov.pl/pjp-api/rest/station/findAll")
        try:
            api = json.loads(api_request.content)
            api2 = json.loads(api_request2.content)
        except Exception:
            api = "Błąd Wczytywania!"
            api2 = "Błąd Wczytywania!"

        return render(request, 'home.html', {'api': api, 'api2': api2,})


    else:
        api_request = requests.get("https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/")
        api_request2 = requests.get("https://api.gios.gov.pl/pjp-api/rest/station/findAll")
        try:
            api = json.loads(api_request.content)
            api2 = json.loads(api_request2.content)
        except Exception as e:
            api = "Błąd Wczytywania!"
            api2 = "Błąd Wczytywania!"

        return render(request, 'home.html', {'api': api, 'api2': api2,})

def about(request):
    return render(request, 'about.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def posts(request):
    posts = Post.published.all()
    return render(request, 'posts.html', {'posts': posts})

