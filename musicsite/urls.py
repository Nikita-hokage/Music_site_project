from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainstr, name='main'),
    path('404', views.getnotFound),
    path('add_page/', views.add_page, name='add_page'),
    path('add_song/', views.add_song, name='add_song'),
    path('add_author/', views.add_author, name='add_author'),
]