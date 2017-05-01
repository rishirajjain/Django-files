from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.ListPost.as_view() ,name ='index'  ),
    url(r'^(?P<pk>[0-9]+)' ,views.ListPost.as_view() ,name ='Post'),
    url(r'^detail/(?P<pk>[0-9]+)$' ,views.detailview.as_view(), name='details'),
    url(r'^delete/(?P<pk>[0-9]+)$' ,views.DeletePost.as_view(), name='deletepost'),


]