# Generated by Django 3.2.13 on 2022-04-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSite', '0006_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
