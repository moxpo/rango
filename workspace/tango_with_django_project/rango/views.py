from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def index(request):
    response = HttpResponse("Rango says hey there partner! Visit the <a href='/rango/about/'>about</a> page.")
    return response
def about(request):
    response = HttpResponse("This is the about page. Go back to the <a href='/rango/'>index</a> page.")
    return response