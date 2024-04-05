# Generated by Django 5.0.2 on 2024-03-26 09:49

import blog_page.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_page', '0002_alter_post_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(validators=[blog_page.models.validate_age]),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, validators=[blog_page.models.validate_bad_words]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[blog_page.models.validate_email, django.core.validators.EmailValidator(message='Enter a valid email')]),
        ),
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]