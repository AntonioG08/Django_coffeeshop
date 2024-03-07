from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})


# With this, instead of getting all the elements from the categories' database, we are pulling only the elements
# from the category we want, using the category ID"""
"""def category(request, category_id):
    category2 = Category.objects.get(id=category_id)
    return render(request, "blog/category.html", {'category': category2})"""


# This way is better, because if the user request an ID that doesn´t exists, which can happen, the server will
# automatically show a '404' response view since that ID doesn't exist, and therefore the url either. Also, this way
# We are filtering the shown posts by the categories, however this is still not the 'best' solution
"""def category(request, category_id):
    category2 = get_object_or_404(Category, id=category_id)
    ' With this we can pull all the posted objects, but filtering by the Category, using the category ID retrieved '
    posts = Post.objects.filter(categories=category2)
    return render(request, "blog/category.html", {'category': category2,
                                                  'posts': posts}) """


def category(request, category_id):
    category2 = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category': category2})
