# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from rest_framework.generics import ListAPIView

from items import models
from . import serializers


class ItemList(ListAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
