# Generated by Django 5.0.2 on 2024-03-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField()),
                ('json', models.JSONField()),
                ('webpage', models.URLField()),
                ('photo', models.BinaryField()),
                ('active', models.BooleanField()),
            ],
        ),
    ]
