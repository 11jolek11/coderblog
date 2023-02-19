from django.shortcuts import render
from django.views import generic
from blog import models
from typing import Any, Dict

# Create your views here.
def index(request):
    """View function of index page."""
    count_blog = models.Blog.objects.count()
    count_authors = models.BlogAuthor.objects.count()

    context = {
        'count_blog': count_blog,
        'count_authors': count_authors,
    }

    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = models.Blog
    context_object_name = 'blog_list'
    paginate_by = 10
