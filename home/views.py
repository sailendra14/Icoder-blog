from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World")

def contact(request):
    return HttpResponse("Contact us page")

def about(request):
    return HttpResponse("About us page")
