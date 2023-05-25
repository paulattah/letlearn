from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.Loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name= 'room'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
 
    
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<int:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<int:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<int:pk>/', views.deleteMessage, name='delete-message'),
]
    