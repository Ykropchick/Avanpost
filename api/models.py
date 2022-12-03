from django.db import models


def upload_to(instance, filename):
    return 'images/tests/{filename}'.format(filename=filename)


def upload_category_to(instance, filename):
    return 'category/{filename}'.format(filename=filename)


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="name")
    imageUrl = models.ImageField(upload_to=upload_category_to, null=True, verbose_name="imageUrl")

    def __str__(self):
        return self.name

class PhotoModel(models.Model):
    imageUrl = models.ImageField(upload_to=upload_to, blank=True, null=True)
    name = models.ManyToManyField(CategoryModel)

