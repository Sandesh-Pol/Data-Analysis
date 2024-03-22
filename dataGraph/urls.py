from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mobile/', views.mobile, name='mobile'),
    path('youtube/', views.youtube, name='youtube'),
    path('metro/', views.metro, name='metro'),
    path('stock/', views.stock, name='stock'),
    path('worldcup/', views.worldcup, name='worldcup'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register_user'),
 
]
