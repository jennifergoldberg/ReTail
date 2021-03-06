# Generated by Django 3.1.2 on 2021-09-08 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.TextField(blank=True, max_length=500)),
                ('bio', models.TextField(blank=True, max_length=2500)),
                ('location', models.TextField(max_length=500)),
                ('org_name', models.TextField(blank=True, max_length=500)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_name', models.TextField(max_length=500)),
                ('image', models.TextField(max_length=500)),
                ('image_two', models.TextField(blank=True, max_length=500)),
                ('image_three', models.TextField(blank=True, max_length=500)),
                ('bio', models.TextField(max_length=2500)),
                ('color', models.TextField(blank=True, max_length=500)),
                ('gender', models.TextField(blank=True, max_length=500)),
                ('friendly', models.TextField(blank=True, max_length=500)),
                ('kids', models.TextField(blank=True, max_length=500)),
                ('age', models.TextField(blank=True, max_length=500)),
                ('breed', models.TextField(blank=True, max_length=500)),
                ('size', models.TextField(blank=True, max_length=500)),
                ('health', models.TextField(blank=True, max_length=500)),
                ('active', models.TextField(blank=True, max_length=500)),
                ('house_trained', models.BooleanField(blank=True, default=False)),
                ('available', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2500)),
                ('created_at', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='main_app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
