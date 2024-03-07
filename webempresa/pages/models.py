from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido", max_length=200)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # With this, the register saves the date when its updated. By default, Django hides this to avoid modifications
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima modificación")

    # This class is used to change the public name of the model in the 'admin' section
    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ["order", "title"]  # puting a '-' indicates to go from newer to older

    # With this function we request to show the title as the public name, instead of a generic project name
    def __str__(self):
        return self.title

