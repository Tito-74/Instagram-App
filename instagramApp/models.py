from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.user

    #Save image
    def save_profile(self):
        self.save()

    #Delete image
    def delete_profile(self):
        self.delete()
   



class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=80)
    caption = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, blank=True,on_delete=models.CASCADE)
    likes = models.ManyToManyField( User, related_name = 'likes', blank=True)
    # comments = models.ForeignKey(Comments, blank=True,on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    #Save image
    def save_post(self):
        self.save()

    #Delete image
    def delete_post(self):
        self.delete()

    def get_post_by_id(cls,id):
        post = cls.objects.get(id=id)
        return post

    @classmethod
    def get_single_photo(cls,id):
        post = cls.objects.get(pk=id)
        return post

    @classmethod
    def search_profile_post(cls,profile):
        profile = cls.objects.filter(profile__user__icontain = profile)
        return profile

    # @classmethod
    # def get_profile_post(cls, profile):
    #     post = Post.objects.filter(profile__pk=profile)
    #     return post  

class Comments(models.Model):
    comment = models.TextField(blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    #Save comment
    def save_comment(self):
        self.save()

    #Delete comment
    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments

    
