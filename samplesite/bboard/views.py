from django.shortcuts import render

# Create your views here.
from .models import Bb

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html',{'bbs':bbs})