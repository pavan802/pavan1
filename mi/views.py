from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mi(request):
    return HttpResponse('<h2>mi owner ambani</h2>')
