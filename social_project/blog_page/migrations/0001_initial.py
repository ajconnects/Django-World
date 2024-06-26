# Generated by Django 5.0.2 on 2024-03-26 09:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField(blank=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('joined_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['username', '-joined_at'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('visibility', models.CharField(choices=[('public', 'public'), ('private', 'private')], default='public', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_page.user')),
            ],
        ),
    ]
