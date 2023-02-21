from django.shortcuts import render
from django.views import generic
from blog import models
from typing import Any, Dict
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404



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
    """
    Blog list view. List of all blogs
    """
    model = models.Blog
    context_object_name = 'blog_list'
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    """
    View of single blog post with details.
    """
    model = models.Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'

class BlogCommentCreate(LoginRequiredMixin, generic.edit.CreateView):
    """
    View for creating new comment
    """
    model = models.BlogComment
    fields = ['description',]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(models.Blog, pk = self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(models.Blog, pk = self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})

class BloggersListView(generic.ListView):
    """
    View of all bloggers publishing on the platform
    """
    model = models.BlogAuthor
    template_name = 'blog/bloggers_list.html'
    context_object_name = 'bloggers_list'

class BloggersDetailView(generic.DetailView):
    """
    View of single blogger with details.
    """
    # Blog.objects.all().filter(author_id=1)
    model = models.BlogAuthor
    context_object_name = 'author'
    template_name = 'blog/author_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors_blog_list'] = models.Blog.objects.all().filter(author_id=self.kwargs['pk'])
        context['authors_blog_list'].order_by('-post_date')
        return context
