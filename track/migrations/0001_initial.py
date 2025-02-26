# Generated by Django 3.1.6 on 2021-02-21 08:21

from django.db import migrations, models
import django.db.models.deletion
import track.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('released', models.CharField(max_length=4)),
                ('picture', models.FileField(upload_to=track.models.cover_path)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('picture', models.FileField(upload_to=track.models.artist_path)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('track_file', models.FileField(upload_to=track.models.track_path)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='track.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(related_name='albums', to='track.Artist'),
        ),
    ]
