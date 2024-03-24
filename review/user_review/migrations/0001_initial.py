# Generated by Django 5.0.2 on 2024-03-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField()),
            ],
            options={
                'db_table': 'User Review',
            },
        ),
    ]
