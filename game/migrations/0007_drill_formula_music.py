# Generated by Django 3.2.13 on 2022-05-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_drill_formula_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='drill_formula',
            name='music',
            field=models.FileField(blank=True, null=True, upload_to='Drills-Music/'),
        ),
    ]
