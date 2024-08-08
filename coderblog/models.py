from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "#" + self.user.username

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)
        else:
            super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-posted_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=32, blank=False, default=None)
    author_email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:15] + "#" + self.author_email

    class Meta:
        ordering = ['-created_at']
