# Generated by Django 4.1.3 on 2022-12-07 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_menu_day_menu_date_menu_meal_plan_delete_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]