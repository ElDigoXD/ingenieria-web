# Generated by Django 5.0 on 2024-01-15 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IW', '0004_food_food_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='gender',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdata',
            name='year_of_birth',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]