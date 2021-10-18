from django.test import TestCase

from .models import Comment, Profile, Image
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    
    def setUp(self):
        self.user = User(username='Kipkorir')
        self.user.save()

        self.profile = Profile(id=12 ,profile_picture='image.jpg', bio='Test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)

class PostTestClass(TestCase):
   
    def setUp(self):
        self.user = User.objects.create_user("username", "password")
        self.new_profile = Profile(id = 12,profile_picture='image.png',bio='Test profile',user=self.user)
        self.new_profile.save()
        self.new_image = Image(image='image.png',image_caption="image", image_profile=self.new_profile)

    def test_instance_true(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_post(self):
        self.new_post.save_image()
        post = Post.objects.all()
        self.assertTrue(len(post) == 1)

    def test_delete_post(self):
        self.new_post.save_image()
        post = Profile.objects.all()
        self.assertTrue(len(post) <= 1)

    def test_get_post_by_id(self):
        self.new_post.save_post()
        post = self.new_post.get_post_by_id(self.new_post.id)
        posts = Image.objects.filter(id=self.new_post.id)
        self.assertTrue(post, posts)    

