# Generated by Django 3.2.13 on 2022-07-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0022_auto_20220623_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='Create_at',
            field=models.DateTimeField(blank=True, max_length=255, null=True),
        ),
    ]
