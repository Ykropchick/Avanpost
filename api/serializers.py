
from rest_framework import serializers
from .models import CategoryModel, PhotoModel


class CategorySerializer(serializers.ModelSerializer):
    imageUrl = serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = CategoryModel
        fields = ['name', 'imageUrl']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ['imageUrl']
