from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def start(request):
    return HttpResponse("<a href='app1'>to Board</a>")