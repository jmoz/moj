# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from items import factories


class ItemTestCase(TestCase):
    def setUp(self):
        self.item = factories.ItemFactory.create(name="Foo", code="FOO", price="13.37")

    def test_price_has_currency(self):
        self.assertEqual("£13.37", self.item.price_text)

    def test_display_name(self):
        self.assertEqual("Foo FOO £13.37", unicode(self.item))
