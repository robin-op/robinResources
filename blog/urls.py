from django.conf.urls import include, url
<<<<<<< HEAD
from . import views
=======
from . import views 
from . import views as core_views
>>>>>>> master
from django.urls import include, path
from django.views.generic import TemplateView

app_name ='blog'
urlpatterns = [
    url(r'^$', views.main,name='home'),
    url(r'^listaPersonajes$', views.listaPersonajes,name='personajes'),
    url(r'^signup$', views.signup,name='signup'),
<<<<<<< HEAD


=======
    url(r'^tierList$', views.tierlist,name='tierlist'),
>>>>>>> master

]
