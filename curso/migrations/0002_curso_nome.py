# Generated by Django 4.0.6 on 2024-04-20 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='nome',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
