# Generated by Django 4.1.7 on 2023-03-28 06:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='context_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Context'),
        ),
        migrations.AddField(
            model_name='news',
            name='context_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Context'),
        ),
        migrations.AddField(
            model_name='news',
            name='context_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Context'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
    ]
