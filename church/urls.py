from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/indexa', views.indexa, name='indexa'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('reqchat', views.reqchat, name='reqchat'),
    path('<str:conversation>/', views.conversation, name='conversation'),
    path('seenokay', views.seenokay, name='seenokay'),
    path('share', views.share, name='share'),
    path('getUtalks/<str:conversation>/', views.getUtalks, name='getUtalks'),
    path('letter', views.letter, name='letter'),
    path('index/indexa/lettera', views.lettera, name='lettera'),
]