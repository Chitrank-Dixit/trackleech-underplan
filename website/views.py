# Create your views here.

from django.shortcuts import render_to_response

from website.models import posts
#from models import posts

# remember the request defined in TrackLeech/urls.py
def home(request):
    return render_to_response('index.html')

