# Generated by Django 3.2.13 on 2022-05-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_remove_drill_formula_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='drill_formula',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='Drills-shape/'),
        ),
    ]