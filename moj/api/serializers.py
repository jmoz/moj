from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()
    price = serializers.CharField()
    display_text = serializers.CharField(source='__unicode__')
