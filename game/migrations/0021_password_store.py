# Generated by Django 3.2.13 on 2022-06-08 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0020_auto_20220608_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password_store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Password', models.TextField(blank=True, null=True)),
                ('Password2', models.CharField(blank=True, max_length=255, null=True)),
                ('Create_at', models.CharField(blank=True, max_length=255, null=True)),
                ('GetPlayer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game_user')),
            ],
        ),
    ]
