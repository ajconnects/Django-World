# Generated by Django 5.0.2 on 2024-03-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksrecords', '0003_booksdetails_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksdetails',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
