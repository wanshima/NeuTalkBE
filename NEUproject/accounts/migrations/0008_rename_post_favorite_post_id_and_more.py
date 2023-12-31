# Generated by Django 4.2.7 on 2023-11-28 04:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_favorite"),
    ]

    operations = [
        migrations.RenameField(
            model_name="favorite",
            old_name="post",
            new_name="post_id",
        ),
        migrations.AlterUniqueTogether(
            name="favorite",
            unique_together={("user", "post_id")},
        ),
    ]
