# Generated by Django 5.0.2 on 2024-03-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storagedetails', '0003_alter_book_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
