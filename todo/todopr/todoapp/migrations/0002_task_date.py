# Generated by Django 4.1.7 on 2023-03-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default='2000-09-22'),
            preserve_default=False,
        ),
    ]