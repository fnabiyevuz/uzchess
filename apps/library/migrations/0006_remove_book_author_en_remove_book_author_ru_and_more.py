# Generated by Django 4.1.7 on 2023-03-28 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_author_full_name_en_author_full_name_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_en',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_ru',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_uz',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category_ru',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category_uz',
        ),
    ]