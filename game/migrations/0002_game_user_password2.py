# Generated by Django 3.2.13 on 2022-05-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_user',
            name='Password2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]