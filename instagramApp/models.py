from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=200, blank=True)

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=80)
    caption = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, blank=True,on_delete=models.CASCADE)
    likes = models.ManyToManyField( User, related_name = 'likes', blank=True)
    # comments = models.CharField(max_length=100, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    #Save image
    def save_post(self):
        self.save()

    #Delete image
    def delete_post(self):
        self.delete()

    # @classmethod
    # def get_profile_images(cls, profile):
    #     images = Image.objects.filter(profile__pk=profile)
    #     return images  

class Comments(models.Model):
    comment = models.TextField(blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    time_posted = models.DateTimeField(auto_now_add=True)

    
