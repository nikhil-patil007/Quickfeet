# Generated by Django 3.2.13 on 2022-05-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_drill_formula_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drill_formula',
            name='music',
            field=models.FileField(default='Drills-Music/sound-effect.mp3', upload_to='Drills-Music/'),
        ),
    ]
