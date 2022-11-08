from django.test import TestCase
from .models import Add_news
from django.urls import reverse
# Create your tests here.
class Add_newsModelTest(TestCase):
    def setUp(self):
        Add_news.objects.create(title='Mavzu', text='Yangilik matni')

    def test_text_content(self):
        news = Add_news.objects.get(id=1)
        expected_object_title = f'{news.title}'
        expected_object_text = f'{news.text}'
        self.assertEqual(expected_object_title, 'Mavzu')
        self.assertEqual(expected_object_text, 'Yangilik matni')

class HomePageViewTest(TestCase):
    def setUp(self):
        Add_news.objects.create(title='Mavzu 2', text='2 Yangilik')

    def test_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_ulr_for_revers(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_ulr_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

