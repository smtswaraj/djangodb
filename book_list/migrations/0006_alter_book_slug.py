# Generated by Django 4.1.7 on 2023-03-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_list', '0005_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
