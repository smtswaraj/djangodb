# Generated by Django 4.1.7 on 2023-03-15 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_list', '0002_rename_reting_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(max_length=50),
        ),
    ]