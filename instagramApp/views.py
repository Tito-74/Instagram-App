from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    return render(request,'home.html')


def created_post(request):
    
    return render(request, 'post.html')
