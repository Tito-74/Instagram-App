from django.shortcuts import render
from django.http import HttpResponse
from instagramApp.models import Post,Profile,Comments

# Create your views here.
def index(request):
    posts = Post.objects.all()
    profile = Profile.objects.all()
    comments = Comments.objects.all()

    return render(request,'home.html', {'posts':posts,'profile':profile ,'comments':comments})


def created_post(request):

    return render(request, 'post.html')

def search_results(request):

    return render(request, 'all-instagram/search.html')
