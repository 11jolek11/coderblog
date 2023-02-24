from rest_framework import serializers
from blog.models import Blog, BlogComment, BlogAuthor


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=15)
    descritption = serializers.CharField()
    post_date = serializers.DateField()
    author = serializers.HyperlinkedRelatedField(
        # read_only = True,
    )
    author_by_name = serializers.SlugRelatedField(
        read_only = True,
        slug_field='name'
    )

    class Meta:
        model = Blog
        fields = ['id', 'name', 'description', 'post_date', 'author_by_name', 'author']
