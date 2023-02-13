from django.contrib import admin
from blog.models import Blog, BlogAuthor, BlogComment

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)