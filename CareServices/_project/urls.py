from django.contrib import admin
from django.urls import path
from nejlepsiProjekt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),  # Hlavní stránka
    path('home/', views.home, name='home'),  # Domácí stránka
]
