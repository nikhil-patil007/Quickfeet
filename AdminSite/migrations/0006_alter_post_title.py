# Generated by Django 3.2.13 on 2022-04-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSite', '0005_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
