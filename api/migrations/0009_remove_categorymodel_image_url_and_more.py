# Generated by Django 4.1.3 on 2022-12-03 21:21

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_categorymodel_imageurl_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='image_url',
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='imageUrl',
            field=models.ImageField(null=True, upload_to=api.models.upload_category_to, verbose_name='imageUrl'),
        ),
    ]
