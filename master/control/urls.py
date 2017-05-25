from django.conf.urls import url
from master.control import views

urlpatterns = [
    url(r'^$', views.articles_list, name='articles-list'),
    url(r'^signin/$', views.singin, name='signin'),
    url(r'^signout/$', views.singout, name='signout'),
    url(r'^update/(?P<pk>\d+)/$', views.update_article, name='update-article'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail_article, name='detail-article'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_article, name='delete-article'),
    url(r'^testing/(?P<pk>\d+)/$', views.update_article2, name='up2'),

]
