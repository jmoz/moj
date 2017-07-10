# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['code']

    @property
    def price_text(self):
        return "£{}".format(self.price)

    def __unicode__(self):
        return "{} {} {}".format(self.name, self.code, self.price_text)