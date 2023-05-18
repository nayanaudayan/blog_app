from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('index/', views.index_view, name='index'),
    path('base/', views.base_view, name='base'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about_view, name='about'),
    path('login/signup/', views.signup_view, name='signup'),
    path('post_detail/', views.postdetail_view, name='post_detail'),
    path('addpost/', views.addpost_view, name='addpost'),
    path('popular/', views.popular_view, name='popular'),



]
