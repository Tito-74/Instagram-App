from django import forms
from  .models import Profile,Comments,Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from urllib import request
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','name','caption']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','profile_photo','bio']
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']