# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from items import factories


class ItemListTestCase(APITestCase):
    def setUp(self):
        factories.ItemFactory.create(name="Foo", code="FOO", price="13.37")
        factories.ItemFactory.create(name="Bar", code="BAR", price="10.00")

    def test_list(self):
        response = self.client.get(reverse('api-list'))

        self.assertEqual(2, len(response.data))
        self.assertIn('name', response.data[0])
        self.assertIn('code', response.data[0])
        self.assertIn('price', response.data[0])
        self.assertIn('display_text', response.data[0])
        self.assertEqual('Bar BAR £10.00', response.data[0]['display_text'])