from django.views.generic import ListView, DetailView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    # context_object_name = 'all_posts_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
