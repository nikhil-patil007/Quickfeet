# Generated by Django 3.0 on 2023-02-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSite', '0009_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_data',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]