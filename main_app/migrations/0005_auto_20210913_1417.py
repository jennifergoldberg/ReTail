# Generated by Django 3.1.2 on 2021-09-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210912_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='bio',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='post',
            name='size',
            field=models.IntegerField(blank=True),
        ),
    ]
