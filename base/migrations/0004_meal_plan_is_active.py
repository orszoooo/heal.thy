# Generated by Django 4.1.3 on 2022-12-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_meal_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal_plan',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]