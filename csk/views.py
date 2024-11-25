from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def csk(request):
    return HttpResponse("<h1>captain of csk is ruturaj </h1>")