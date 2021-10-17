from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    url('^$',views.index,name = 'home'),
    url(r'^post/',views.created_post, name = 'post'),
    url(r'^search/', views.search_results, name='search_results'),
    path('registration/', views.registerPage, name="registration"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)