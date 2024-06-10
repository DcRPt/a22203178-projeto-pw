# Generated by Django 4.0.6 on 2024-04-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_remove_album_number_songs_remove_album_release_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='number_of_songs',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='album',
            name='release_year',
            field=models.IntegerField(default='2024'),
        ),
        migrations.AddField(
            model_name='band',
            name='nationality',
            field=models.CharField(default='Português', max_length=100),
        ),
        migrations.AddField(
            model_name='band',
            name='num_members',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='band',
            name='year_start',
            field=models.IntegerField(default='2024'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, default='0', null=True, upload_to='album_covers/'),
        ),
        migrations.AlterField(
            model_name='band',
            name='photo',
            field=models.ImageField(blank=True, default='0', null=True, upload_to='band_photos'),
        ),
        migrations.AlterField(
            model_name='song',
            name='spotify_link',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
