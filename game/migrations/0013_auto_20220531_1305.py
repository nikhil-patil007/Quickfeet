# Generated by Django 3.2.13 on 2022-05-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_auto_20220531_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='Avg_Time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scorebord',
            name='Avg_Time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]