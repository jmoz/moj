import factory

from . import models


class ItemFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Item
