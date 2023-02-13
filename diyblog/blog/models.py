from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# TODO: Fill get_absolute_url
class BlogAuthor(models.Model):
    """
    Class representing author (of comment) entity
    """
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50, help_text="Write about yourself here!")
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse()

class Blog(models.Model):
    """
    Class representing blog article entity 
    """
    name = models.CharField(max_length=15)
    descritption = models.TextField()
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.name} written by {self.author}'

    def get_absolute_url(self) -> str:
        return reverse()

class BlogComment(models.Model):
    """
    Class representing comment entity for a blog article
    """
    description = models.CharField(max_length=50)
    post_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'Comment on {self.blog} by {self.author}'
