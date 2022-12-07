# Generated by Django 4.1.3 on 2022-12-07 19:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_meal_plan_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='day',
        ),
        migrations.AddField(
            model_name='menu',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='meal_plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.meal_plan'),
        ),
        migrations.DeleteModel(
            name='Day',
        ),
    ]
