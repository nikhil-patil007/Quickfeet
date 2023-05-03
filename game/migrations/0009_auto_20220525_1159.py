# Generated by Django 3.2.13 on 2022-05-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_alter_drill_formula_music'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drill_formula',
            name='music',
        ),
        migrations.AddField(
            model_name='add_players',
            name='age',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='game_user',
            name='age',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
