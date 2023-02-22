from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Blog, BlogAuthor, BlogComment



# Create your tests here.
class BlogAuthorTestCase(TestCase):
    """
    Test for model BlogAuthor
    """
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_user_create = User(username='testuser', password='gf*fvASF432fb')
        cls.test_user_create.save()
        cls.test_author_create = BlogAuthor.objects.create(name=cls.test_user_create, bio='Test bio')
        cls.test_author_create.save()
    
    def setUp(self) -> None:
        self.test_user = User.objects.get(id=1)
        self.test_author = BlogAuthor.objects.get(bio='Test bio')
        return super().setUp()
    
    def test_bio_length(self):
        self.assertEqual(BlogAuthor.bio.field.max_length, 50)

    def test_object_name(self):
        self.assertEqual(str(self.test_author), 'testuser')

    def test_url(self):
        self.assertEqual(self.test_author.get_absolute_url(), f'/blog/blogger/{self.test_author.id}')

    def test_name_label(self):
        field_label = self.test_author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_bio_label(self):
        field_label = self.test_author._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

class BlogTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_user_create = User(username='testuser', password='gf*fvASF432fb')
        cls.test_user_create.save()
        cls.test_author_create = BlogAuthor.objects.create(name=cls.test_user_create, bio='Test bio')
        cls.test_author_create.save()

    def setUp(self) -> None:
        self.test_author = BlogAuthor.objects.get(bio='Test bio')
        self.test_blog_post = Blog.objects.create(name='Test1 blog post', descritption="Test1 blog post descritption", author=self.test_author)
        return super().setUp()
   
    def test_name_length(self):
        self.assertEqual(Blog.name.field.max_length, 15)

    def test_object_name(self):
        self.assertEqual(str(self.test_blog_post), f'{self.test_blog_post.name} written by {self.test_blog_post.author.name}')

    def test_url(self):
        self.assertEqual(self.test_blog_post.get_absolute_url(), f'/blog/{self.test_blog_post.id}')

    def test_name_label(self):
        field_label = self.test_blog_post._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'title')

    def test_descritption_label(self):
        field_label = self.test_blog_post._meta.get_field('descritption').verbose_name
        self.assertEqual(field_label, 'descritption')

    def test_author_label(self):
        field_label = self.test_blog_post._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_post_date_label(self):
        field_label = self.test_blog_post._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label, 'post date')

class BlogCommentTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_user_create = User(username='testuser', password='gf*fvASF432fb')
        cls.test_user_create.save()
        cls.test_author_create = BlogAuthor.objects.create(name=cls.test_user_create, bio='Test bio')
        cls.test_author_create.save()        

    def setUp(self) -> None:
        self.test_author = BlogAuthor.objects.get(bio='Test bio')
        self.test_blog_post = Blog.objects.create(name='Test1 blog post', descritption="Test1 blog post descritption", author=self.test_author)
        self.test_blog_comment = BlogComment.objects.create(description='first test comment for firts blog post', author=self.test_user_create, blog=self.test_blog_post)
        return super().setUp()

    def test_description_length(self):
        self.assertEqual(BlogComment.description.field.max_length, 50)
 