from django.test import TestCase
from django.urls import reverse



# Create your tests here.

# Tests of views 
class SignUpCreateViewTest(TestCase):
    def test_view_url_at_expected_location(self):
        response = self.client.get('/accoutns/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_tempalte(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

# Tests of models
