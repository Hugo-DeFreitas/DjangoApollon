# Generated by Django 3.0 on 2019-12-25 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_confirmation_token_on_user_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='playlists_followed', to='app.UserProfile'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, related_name='playlists', to='app.Song'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='confirmation_token',
            field=models.CharField(blank=True, default='1ztw1Pj3VprgZdsvYTDozsyu2PrpGn6k', max_length=32, null=True),
        ),
    ]