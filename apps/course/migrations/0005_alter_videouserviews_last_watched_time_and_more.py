# Generated by Django 4.1.7 on 2023-03-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_videouserviews_viewed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videouserviews',
            name='last_watched_time',
            field=models.DurationField(blank=True, null=True, verbose_name='Last Watched Time'),
        ),
        migrations.AlterField(
            model_name='videouserviews',
            name='progress',
            field=models.IntegerField(blank=True, null=True, verbose_name='Progress'),
        ),
    ]
