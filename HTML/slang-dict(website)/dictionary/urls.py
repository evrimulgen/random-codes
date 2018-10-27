from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.kelime_listesi, name='kelime_listesi'),
    url(r'^kelime/(?P<pk>\d+)/$', views.kelime_detail, name='kelime_detail'),
    url(r'^kelime/new/$', views.post_new, name='post_new'),
    url(r'^kelime/(?P<pk>\d+)/editle/$', views.kelime_editle, name='kelime_editle'),
]