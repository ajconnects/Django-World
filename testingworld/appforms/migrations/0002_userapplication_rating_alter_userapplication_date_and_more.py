# Generated by Django 5.0.1 on 2024-04-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appforms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userapplication",
            name="rating",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="userapplication",
            name="date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="userapplication",
            name="phone",
            field=models.CharField(max_length=15),
        ),
    ]
