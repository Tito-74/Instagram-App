from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'home'),
    url(r'^post/',views.created_post, name = 'post'),
]