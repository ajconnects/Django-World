# Generated by Django 5.0.2 on 2024-03-10 19:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksrecords', '0002_booksdetails_title_alter_booksdetails_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksdetails',
            name='rating',
            field=models.IntegerField(default=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)]),
        ),
    ]