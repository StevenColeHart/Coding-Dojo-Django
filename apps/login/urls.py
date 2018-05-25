from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^add$', views.add),
    url(r'^logout$', views.logout),
    url(r'^user/(?P<id>[0-9]+)$', views.user),
    url(r'^fav/(?P<id>[0-9]+)$', views.fav),
    url(r'^drop/(?P<id>[0-9]+)$', views.drop),
    url(r'^new$', views.new),
]