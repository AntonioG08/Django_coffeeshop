"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contact.urls')),
    path('page/', include('pages.urls')),
    path('services/', include('services.urls')),
]

# With this we are able to see images that are stored in the 'admin' section
if settings.DEBUG:
    from django.conf.urls.static import static
    # With this the user is able to visualize an image when he clicks it, a page will pop up and show the image
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
