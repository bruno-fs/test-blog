from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Post

# return list of posts ordered by published date
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

# get details for individual posts or 404 page
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
