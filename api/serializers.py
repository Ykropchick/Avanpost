
from rest_framework import serializers
from .models import CategoryModel, PhotoModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['name', 'image_url']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ['photo']
