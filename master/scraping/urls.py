from django.conf.urls import url
from master.scraping import views

urlpatterns = [
    url(r'^$', views.map_view, name='map'),
    url(r'^all/$', views.posts, name='main'),
    url(r'^about/$', views.about, name='about'),
    url(r'^select_category/$', views.select_category, name='select-category'),
    url(r'^by_category/(?P<id>\d+)/$', views.by_category, name='by-category'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail_article, name='detail-article'),

]
