from django.contrib import admin
from .models import *


@admin.register(PhotoModel)
class PhotoModelAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    pass