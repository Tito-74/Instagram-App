from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from instagramApp.models import Post,Profile,Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form =UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                # messages.success(request,'Account was created successfully')
                return redirect('login')
        context = {'form': form}
        return render(request,'registration/registration_form.html',  context)


def index(request):
    posts = Post.objects.all()
    profile = Profile.objects.all()
    comments = Comments.objects.all()

    return render(request,'home.html', {'posts':posts,'profile':profile ,'comments':comments})


def created_post(request):

    return render(request, 'post.html')

def search_results(request):

    return render(request, 'all-instagram/search.html')
