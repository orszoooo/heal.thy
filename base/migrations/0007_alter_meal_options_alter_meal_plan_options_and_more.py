# Generated by Django 4.1.3 on 2022-12-10 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_menu_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='meal_plan',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='meal_plan',
            name='updated',
        ),
        migrations.AddField(
            model_name='meal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]