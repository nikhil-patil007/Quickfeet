# Generated by Django 3.2.13 on 2022-06-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_auto_20220531_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='drill_formula',
            name='music',
            field=models.FileField(blank=True, default='sound-effect.mp3', max_length=255, null=True, upload_to='Drills-Music/'),
        ),
    ]