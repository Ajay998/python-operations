# Generated by Django 5.0 on 2024-01-02 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('photo', models.ImageField(upload_to='music_photos')),
                ('musicfile', models.FileField(upload_to='music_files')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.artist')),
                ('genres', models.ManyToManyField(to='app.genre')),
            ],
        ),
    ]
