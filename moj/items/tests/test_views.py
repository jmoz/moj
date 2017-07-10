from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from items import factories


class ItemsListTestCase(TestCase):
    def setUp(self):
        factories.ItemFactory.create(name="Foo", code="FOO", price="13.37")
        factories.ItemFactory.create(name="Bar", code="BAR", price="10.00")
        self.client = Client()

    def test_list(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(2, len(response.context['object_list']))
        self.assertIn("Foo", response.content.decode('utf8'))
        self.assertIn("Bar", response.content.decode('utf8'))
