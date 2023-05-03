# Generated by Django 3.2.13 on 2022-12-15 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0032_contact_us_contact_us_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country_codes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Alpha_3_code', models.CharField(blank=True, max_length=255, null=True)),
                ('Country_code', models.CharField(blank=True, max_length=255, null=True)),
                ('Create_at', models.DateField(auto_now_add=True)),
                ('Update_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
