# Generated by Django 4.2.5 on 2023-09-23 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeentry',
            name='date',
            field=models.DateField(default='1990-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeentry',
            name='hours',
            field=models.IntegerField(default=1),
        ),
    ]