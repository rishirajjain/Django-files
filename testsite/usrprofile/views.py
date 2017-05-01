from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Post


class ListPost(TemplateView):
    template_name = 'usrprofile/home.html'


class List(ListView):
    template_name = 'usrprofile/post.html'
    model = Post

class Dview(DetailView):
    template_name = 'usrprofile/details.html'
