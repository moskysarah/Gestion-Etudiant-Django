from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),  # Page d'accueil
]
