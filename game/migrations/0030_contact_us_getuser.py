# Generated by Django 3.2.13 on 2022-07-11 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0029_auto_20220708_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='GetUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game_user'),
        ),
    ]