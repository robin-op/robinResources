from django.conf.urls import include, url
from . import views
from django.urls import include, path
from django.views.generic import TemplateView

app_name ='personajes'
urlpatterns = [
    url(r'^corrin/$',views.corrin, name="corrin"),
    url(r'^cloud/$',views.cloud, name="cloud"),
    url(r'^ike/$',views.ike, name="ike"),
    url(r'^inkling/$',views.inkling, name="inkling"),
    url(r'^joker/$',views.joker, name="joker"),
    url(r'^lucina/$',views.lucina, name="lucina"),
    url(r'^marth/$',views.marth, name="marth"),
    url(r'^pit/$',views.pit, name="pit"),
    url(r'^roy/$',views.roy, name="roy"),
    url(r'^chrom/$',views.chrom, name="chrom"),
    url(r'^robin/$',views.robin, name="robin"),


]