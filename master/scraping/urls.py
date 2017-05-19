from django.conf.urls import url
from master.scraping import views

urlpatterns = [
    url(r'^$', views.posts, name='main'),
    url(r'^map/$', views.map_view, name='map'),
]
