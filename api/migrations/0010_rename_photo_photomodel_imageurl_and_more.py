# Generated by Django 4.1.3 on 2022-12-03 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_categorymodel_image_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photomodel',
            old_name='photo',
            new_name='imageUrl',
        ),
        migrations.RenameField(
            model_name='photomodel',
            old_name='category',
            new_name='name',
        ),
    ]