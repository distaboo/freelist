# Generated by Django 2.0.5 on 2018-09-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='dateChange',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
