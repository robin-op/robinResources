from django.conf.urls import include, url
from . import views 
from . import views as core_views
from django.urls import include, path
from django.views.generic import TemplateView

app_name ='blog'
urlpatterns = [
    url(r'^$', views.main,name='home'),
    url(r'^listaPersonajes$', views.listaPersonajes,name='personajes'),
    url(r'^signup$', views.signup,name='signup'),
    url(r'^tierList$', views.tierlist,name='tierlist'),
    url(r'^login$', views.login,name='login'),


]
