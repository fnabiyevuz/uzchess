# Generated by Django 4.1.7 on 2023-03-25 07:49

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Full name')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ', verbose_name='Phone number')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('working_time', models.CharField(max_length=255, verbose_name='Working time')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ', verbose_name='Phone number')),
                ('metro', models.CharField(max_length=255, verbose_name='Metro')),
                ('map', models.TextField(verbose_name='Map')),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Infos',
            },
        ),
        migrations.CreateModel(
            name='RulesOfUsing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Rules Of Using',
                'verbose_name_plural': 'Rules Of Usings',
            },
        ),
    ]
