from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #Individual Blog review url regex
    url(r'^review/(?P<blog_id>[0-9]+)/$', views.reviewBlog, name="reviewBlog")
]