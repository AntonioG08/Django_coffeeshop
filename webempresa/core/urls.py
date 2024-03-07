from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('historia/', views.about, name="Historia"),
    path('visitanos/', views.store, name="Visitanos"),
]

