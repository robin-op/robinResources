from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers
from blog.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('blog.urls')),
    url(r'personajes/', include('personajes.urls')),
    url(r'accounts/', include('accounts.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    



]
