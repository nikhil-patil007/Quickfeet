# Generated by Django 3.2.13 on 2022-06-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0019_drill_formula_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_user',
            name='Create_at',
            field=models.DateTimeField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='game_user',
            name='Update_at',
            field=models.DateTimeField(blank=True, max_length=255, null=True),
        ),
    ]
