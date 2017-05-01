from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.ListPost.as_view() ,name ='index'  ),
    url(r'^(?P<pk>[0-9]+)$' ,views.ListPost.as_view() ,name ='Post'),
    url(r'^(?P<pk>[0-9]+)$' ,views.Dview.as_view()),


]