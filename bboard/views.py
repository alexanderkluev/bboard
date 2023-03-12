from django.shortcuts import render, HttpResponse
from .models import Bb

def main_page(request):
    bbs = Bb.objects.order_by('-published')
    return render(request,'bboard/templates/index.html', {'bbs': bbs})
# Create your views here.
