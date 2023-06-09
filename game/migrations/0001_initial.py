# Generated by Django 3.2.13 on 2022-05-18 09:12

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Create_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Via', models.TextField(blank=True, null=True)),
                ('Full_name', models.CharField(blank=True, max_length=255)),
                ('Game_name', models.CharField(blank=True, max_length=255)),
                ('Email', models.EmailField(blank=True, max_length=40)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Gender', models.CharField(choices=[('0', '--'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='0', max_length=10)),
                ('Password', models.TextField(blank=True, null=True)),
                ('Country', models.CharField(blank=True, max_length=255, null=True)),
                ('Shirt_num', models.CharField(blank=True, max_length=255, null=True)),
                ('Is_active', models.CharField(choices=[('1', 'Active'), ('0', 'Deactive')], default='1', max_length=10)),
                ('Otp', models.CharField(blank=True, max_length=10, null=True)),
                ('Create_at', models.CharField(blank=True, max_length=255, null=True)),
                ('Update_at', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, max_length=255, null=True, populate_from='title', unique=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='CkEditor/')),
                ('contain', ckeditor.fields.RichTextField()),
                ('Is_Active', models.CharField(choices=[('1', 'Active'), ('0', 'Deactive')], default='1', max_length=10)),
                ('Create_at', models.CharField(blank=True, max_length=255, null=True)),
                ('Update_at', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drill_Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(blank=True, max_length=255, null=True)),
                ('Condition', models.CharField(blank=True, max_length=255, null=True)),
                ('Create_at', models.DateField(auto_now=True)),
                ('deal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.drills')),
            ],
        ),
        migrations.CreateModel(
            name='Drill_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='Drills/')),
                ('Is_Active', models.CharField(choices=[('1', 'Active'), ('0', 'Deactive')], default='1', max_length=10)),
                ('Create_at', models.DateField(auto_now=True)),
                ('Main', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Main', to='game.drills')),
                ('Main1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Main1', to='game.drills')),
                ('Main2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Main2', to='game.drills')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Token', models.TextField(blank=True, null=True)),
                ('Email', models.CharField(blank=True, max_length=255, null=True)),
                ('Subject', models.CharField(blank=True, max_length=255, null=True)),
                ('Message', models.TextField(blank=True, null=True)),
                ('Is_Active', models.CharField(choices=[('1', 'Active'), ('0', 'Deactive')], default='1', max_length=10)),
                ('Create_at', models.CharField(blank=True, max_length=255, null=True)),
                ('GetPlayer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.game_user')),
            ],
        ),
        migrations.CreateModel(
            name='Add_Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(blank=True, max_length=255)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Country', models.CharField(blank=True, max_length=255, null=True)),
                ('Shirt_num', models.CharField(blank=True, max_length=255, null=True)),
                ('Create_at', models.CharField(blank=True, max_length=255, null=True)),
                ('GetPlayer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game_user')),
            ],
        ),
    ]
