# Generated by Django 4.2.7 on 2023-11-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="thread",
            name="category",
            field=models.CharField(default="Default Category", max_length=50),
        ),
    ]
