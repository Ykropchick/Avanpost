from django.db import models


def upload_to(instance, filename):
    return 'images/tests/{filename}'.format(filename=filename)


def upload_category_to(instance, filename):
    return 'category/{filename}'.format(filename=filename)


class CategoryModel(models.Model):
    category = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to=upload_category_to, null=True)

    def __str__(self):
        return self.category


class PhotoModel(models.Model):
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    category = models.ManyToManyField(CategoryModel)

