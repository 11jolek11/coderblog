from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm


# Create your views here.
def index(request):
    latest_posts_list = Post.objects.order_by("-posted_at")[:25]
    context = {"latest_posts_list": latest_posts_list}
    return render(request, "coderblog/index.html", context)


def post_detail_by_slug(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
                author_name=comment_form.cleaned_data["author_name"],
                author_email=comment_form.cleaned_data["author_email"],
                content=comment_form.cleaned_data["content"],
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    return render(request, "coderblog/post.html", {"post": post, "comments": comments, "form": comment_form})


def post_detail_by_id(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
                author_name=comment_form.cleaned_data["author_name"],
                author_email=comment_form.cleaned_data["author_email"],
                content=comment_form.cleaned_data["content"],
            )
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.path_info)
    return render(request, "coderblog/post.html", {"post": post, "comments": comments, "form": comment_form})
