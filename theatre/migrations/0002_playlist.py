# Generated by Django 2.2.11 on 2022-07-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('public', models.BooleanField(default=False)),
            ],
        ),
    ]
