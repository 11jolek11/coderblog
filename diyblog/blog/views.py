from django.shortcuts import render
from django.views import generic
from blog.models import Blog, BlogAuthor

# Create your views here.
def index(request):
    """View function of index page."""
    # TODO: fill context
    count_blog = Blog.objects.count()
    count_authors = BlogAuthor.objects.count()

    context = {
        'count_blog': count_blog,
        'count_authors': count_authors,
    }

    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    # model = Book
    pass
