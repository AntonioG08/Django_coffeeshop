from django.contrib import admin
from .models import services


# Register your models here.

# With this configuration we can see our model created in the Admin section
class ServicesAdmin(admin.ModelAdmin):
    # With this we can put these elements from the 'models' section as readable
    readonly_fields = ('created', 'updated')


admin.site.register(services, ServicesAdmin)
