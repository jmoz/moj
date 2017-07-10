# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from . import factories


class ItemTestCase(TestCase):
    def setUp(self):
        self.item = factories.ItemFactory.create(name="Foo", code="FOO", price="13.37")

    def test_price_has_currency(self):
        self.assertEqual("£13.37", self.item.price_text)

    def test_display_name(self):
        self.assertEqual("Foo FOO £13.37", unicode(self.item))


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
