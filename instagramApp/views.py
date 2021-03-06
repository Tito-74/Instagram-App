from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from instagramApp.models import Post,Profile,Comments
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm,CommentsForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def registerPage(request):
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

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username ,password=password)
            if user is not None:
                login(request, user)
        context={'form': form}
        return render(request,'registration/login.html',  context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login/')
def index(request):
    posts = Post.objects.all()
    profile = Profile.objects.all()
    comments = Comments.objects.all()

    return render(request,'home.html', {'posts':posts,'profile':profile ,'comments':comments})

@login_required(login_url='login/')
def create_post(request):
    # current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.profile = request.user
            post.user = request.user
            post.save()
        return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post.html', {"form": form})


def search_results(request):
    if 'profile' in request.GET and request.GET['profile']:
        user = request.GET.get("profile")
        print(user)
        results = Profile.search_profile(user)
        message = f'profile'
        return render(request, 'search.html',{'profiles': results,'message': message})
    else:
        message = "You haven't searched for anything, please try again"
    return render(request, 'search.html', {'message': message})

    return render(request, 'all-instagram/search.html')
