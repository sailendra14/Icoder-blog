from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse("This is our blogHome")

def blogPost(request, slug):
    return HttpResponse(f'This is our blog post: {slug}')
