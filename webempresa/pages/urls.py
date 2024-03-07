from django.urls import path
from . import views

""" Since we want to pass an ID number, we need to declare 'int:' before, if we dont do this, Django will sent a string
    and this will not work """
urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name="Page"),
]

