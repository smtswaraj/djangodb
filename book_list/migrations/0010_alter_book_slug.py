# Generated by Django 4.1.7 on 2023-03-19 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_list', '0009_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False),
        ),
    ]
