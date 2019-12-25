# Generated by Django 3.0 on 2019-12-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_update_on_playlist_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='picture',
            field=models.TextField(blank=True, default='/static/img/album-img-not-found.png', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='confirmation_token',
            field=models.CharField(blank=True, default='zzI2xkB5uGhq8qfYR31vVgcdJ5LUudoL', max_length=32, null=True),
        ),
    ]