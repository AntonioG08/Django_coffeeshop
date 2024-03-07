from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here // Here we will learn about the foreign keys and the relations many to many
# Model for the categories that the user can choose for the blog
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    # With this, the register saves the date when its created. By default, Django hides this to avoid modifications
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # With this, the register saves the date when its updated. By default, Django hides this to avoid modifications
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima modificación")

    # This class is used to change the public name of the model in the 'admin' section
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorias"
        ordering = ["-created"]  # puting a '-' indicates to go from newer to older

    # With this function we request to show the title as the public name, instead of a generic project name
    def __str__(self):
        return self.name


# Model with the posts that the users does to the blog
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(max_length=300, verbose_name="Contenido")
    # The author can put a specific date of publishing, or leave it to the default current time from timezone
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    # The variable 'upload_to' allows us to save the images in a separate folder and keep everything organized
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    # This foreign key allows us to pull the user from the user database, and in case the user gets deleted, everything
    # will be erased in CASCADE
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    # This allows us to choose a category from many options. The 'get_posts' is used to filter the blog by categories
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    # With this, the register saves the date when its created. By default, Django hides this to avoid modifications
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # With this, the register saves the date when its updated. By default, Django hides this to avoid modifications
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima modificación")

    # This class is used to change the public name of the model in the 'admin' section
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created"]  # puting a '-' indicates to go from newer to older

    # With this function we request to show the title as the public name, instead of a generic project name
    def __str__(self):
        return self.title
