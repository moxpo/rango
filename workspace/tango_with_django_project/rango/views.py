from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    response = HttpResponse("Rango says hey there partner! Visit the <a href='/rango/about/'>About</a> page.")
    return response
def about(request):
    response = HttpResponse("This is the about page. Go back to the <a href='/rango/'>Index</a> page.")
    return response