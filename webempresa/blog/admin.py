from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # With this we can put these elements from the 'models' section as readable
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    # With this we can put these elements from the 'models' section as readable
    readonly_fields = ('created', 'updated')
    # With this we add the columns 'title', 'author' and 'published' to the admin view of the post model in the blog app
    list_display = ('title', 'author', 'published', 'post_categories')
    # With this we can order the items, first by author and then by 'published'
    ordering = ('author', 'published')
    # With this we can add a search bar that will filter by author or content searched.
    """Since the author itself is another model, we need to specify what we are looking specifically from the 'author'
       model, which in this case is the name of the author or 'username' """
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    # With this we can filter the entries by dates
    date_hierarchy = 'published'
    # With this we can also filter the information by the author's username for example, which can be useful
    list_filter = ('author__username', 'categories__name')

    """Since we can add 'categories' or 'categories__name' to the list display because it doesnt allow a 'many to many'
       we will use the following strategy"""
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    # With this we can change the display name of the function, so we can see the new name in the 'admin' section.
    post_categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
