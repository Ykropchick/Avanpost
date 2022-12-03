
from rest_framework import serializers
from .models import CategoryModel, PhotoModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['name', 'imageUrl']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ['photo']
