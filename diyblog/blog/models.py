from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class BlogAuthor(models.Model):
    """
    Class representing author (of comment) entity
    """
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50, help_text="Write about yourself here!")

    class Meta:
        ordering = ['name', 'bio']
    
    def __str__(self) -> str:
        return self.name.username

    def get_absolute_url(self) -> str:
        return reverse('bloger-detail', args=[str(self.id)])

class Blog(models.Model):
    """
    Class representing blog article entity 
    """
    name = models.CharField(max_length=15, verbose_name='title')
    descritption = models.TextField()
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-post_date']
        permissions = [
            (
                'can_publish',
                'Can publish Blog posts'
            )
        ]
    
    def __str__(self) -> str:
        return f'{self.name} written by {self.author.name.username}'

    def get_absolute_url(self) -> str:
        return reverse('blog-detail', args=[str(self.id)])

class BlogComment(models.Model):
    """
    Class representing comment entity for a blog article
    """
    description = models.CharField(max_length=50)
    post_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date'],
        permissions = [
            (
                'can_comment',
                'Can publish a comment'
            )
        ]
 
    def __str__(self) -> str:
        return f'Comment on {self.blog.name} by {self.author}'
