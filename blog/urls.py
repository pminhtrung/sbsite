from django.conf.urls import patterns, include, url
from . import views, feed

urlpatterns = patterns(
    '',
    url('^$', views.BlogIndex.as_view(), name="index"),
    url('^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url('^feed/$', feed.LatestPosts(), name="feed"),
)