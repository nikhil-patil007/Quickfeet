# Generated by Django 3.2.13 on 2022-04-29 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSite', '0007_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='CkEditor/'),
        ),
    ]