# Generated by Django 5.1.1 on 2024-09-16 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="cover_image",
            field=models.ImageField(blank=True, null=True, upload_to="book_covers/"),
        ),
    ]
