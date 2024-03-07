from django.urls import path
from . import views

""" Since we want to pass an ID number, we need to declare 'int:' before, if we dont do this, Django will sent a string
    and this will not work """
urlpatterns = [
    path('', views.blog, name="Blog"),
    path('category/<int:category_id>/', views.category, name="Category"),
]

