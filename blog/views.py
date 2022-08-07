from django.shortcuts import render
from django.views import generic
from .models import Post


# create view code
class PostList(generic.ListView):
    # setting model to post
    model = Post
    # set this to 1 for posted comments and order in descending by created on
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

