from django.urls import path

from . import views

urlpatterns = [
    path('404', views.getnotFound),
    path('<name>', views.janrGetName),
    path('', views.mainstr, name='main'),
]