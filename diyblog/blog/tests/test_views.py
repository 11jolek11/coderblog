from django.test import TestCase
from django.urls import reverse

from blog.models import Blog, BlogAuthor
from django.contrib.auth.models import User



class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        number_of_blog_posts = 8

        cls.test_user = User(username="testuser", password='gf*fvASF432fb')
        cls.test_user.save()

        cls.test_author_create = BlogAuthor.objects.create(name=cls.test_user, bio='test bio')
        cls.test_author_create.save()

        cls.test_author = BlogAuthor.objects.get(name=cls.test_user)

        for post_number in range(number_of_blog_posts):
            Blog.objects.create(
                name=f'Post nr.{post_number}',
                descritption=f'Content {post_number}',
                author=cls.test_author,
            )
        return super().setUpTestData()
    def test_view_url_at_expected_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_tempalte(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')  

    def test_pagination_works(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blog_list']), 5)
