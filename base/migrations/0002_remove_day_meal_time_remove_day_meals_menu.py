# Generated by Django 4.1.3 on 2022-11-29 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='meal_time',
        ),
        migrations.RemoveField(
            model_name='day',
            name='meals',
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.day')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.meal')),
                ('meal_time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.meal_time')),
            ],
        ),
    ]
