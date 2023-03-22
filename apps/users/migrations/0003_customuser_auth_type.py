# Generated by Django 4.1.7 on 2023-03-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='auth_type',
            field=models.CharField(choices=[('VPH', 'via phone number'), ('VEM', 'via email')], default='VPH', max_length=3),
            preserve_default=False,
        ),
    ]
