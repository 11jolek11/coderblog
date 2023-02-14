from django.shortcuts import render
from blog.models import Blog, BlogAuthor

# Create your views here.
def index(request):
    """View function of index page."""
    # TODO: fill context
    count_blog = Blog.objects.count()
    count_authors = BlogAuthor.objects.count()
    return render(request, 'index.html')
