# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=8, decimal_places=2)
