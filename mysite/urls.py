from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('blog.urls')),
    url(r'personajes/', include('personajes.urls')),
    url(r'accounts/', include('accounts.urls')),

]
