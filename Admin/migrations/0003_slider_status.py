# Generated by Django 4.2.1 on 2023-07-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
