# Generated by Django 3.2.13 on 2022-04-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSite', '0004_rename_body_post_contain'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
