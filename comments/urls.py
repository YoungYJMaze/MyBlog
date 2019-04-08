from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^comment/post/(?P<post_id>[0-9]+)/$', views.post_comment, name='post_comment'),
    url(r'^comment/essay_post/(?P<essay_id>[0-9]+)/$', views.essay_comment, name='essay_comment'),

]