# Generated by Django 3.2.13 on 2022-05-27 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_alter_score_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hits', models.CharField(blank=True, max_length=255, null=True)),
                ('Passing_Time', models.CharField(blank=True, max_length=255, null=True)),
                ('Time_Type', models.CharField(blank=True, max_length=255, null=True)),
                ('Time', models.CharField(blank=True, max_length=255, null=True)),
                ('Avg_Time', models.CharField(blank=True, max_length=255, null=True)),
                ('Score', models.IntegerField(blank=True, null=True)),
                ('Create_at', models.DateField(auto_now=True)),
                ('GetDrill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.drill_data')),
                ('GetPlayer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.game_user')),
            ],
        ),
        migrations.CreateModel(
            name='Scorebord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hits', models.CharField(blank=True, max_length=255, null=True)),
                ('Passing_Time', models.CharField(blank=True, max_length=255, null=True)),
                ('Time_Type', models.CharField(blank=True, max_length=255, null=True)),
                ('Time', models.CharField(blank=True, max_length=255, null=True)),
                ('Avg_Time', models.CharField(blank=True, max_length=255, null=True)),
                ('Score', models.IntegerField(blank=True, null=True)),
                ('Create_at', models.DateField(auto_now=True)),
                ('AddPlayer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.add_players')),
                ('GetDrill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.drill_data')),
                ('GetPlayer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.game_user')),
            ],
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]