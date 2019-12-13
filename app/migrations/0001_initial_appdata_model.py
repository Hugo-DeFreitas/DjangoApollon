# Generated by Django 3.0 on 2019-12-13 11:40

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
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='No description provided', max_length=500, null=True)),
                ('is_public', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbid', models.TextField(blank=True, max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField(blank=True, default='No description provided', max_length=300, null=True)),
                ('is_valid', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Playlist')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile'),
        ),
    ]