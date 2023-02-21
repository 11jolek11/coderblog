from django.contrib import admin
from blog.models import Blog, BlogAuthor, BlogComment

# Register your models here.

# admin.site.register(Blog)
# admin.site.register(BlogAuthor)
# admin.site.register(BlogComment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'author', 'post_date')
    date_hierarchy = 'post_date'
    list_filter = ('author')
    empty_value_display = '--NULL--'

    @admin.display
    def short_name(self, object):
        return object.name[:9] + '...'

@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = ('name')
    empty_value_display = '--NULL--'

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('short_blog_title', 'author', 'post_date')
    empty_value_display = '--NULL--'

    @admin.display
    def short_blog_title(self, object):
        return object.blog.name[:9] + '...'

# admin.site.register(Blog, BlogAdmin)
# admin.site.register(BlogAuthor, BlogAuthorAdmin)
# admin.site.register(BlogComment, BlogCommentAdmin)
