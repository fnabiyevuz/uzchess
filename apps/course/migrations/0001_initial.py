# Generated by Django 4.1.7 on 2023-03-26 14:34

import apps.course.utils
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Chapter',
                'verbose_name_plural': 'Chapters',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('lang_code', models.CharField(choices=[('ru', 'Russian'), ('en', 'English'), ('uz', 'Uzbek')], max_length=3, verbose_name='Language code')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price')),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Discounted price')),
                ('discounted_expire_date', models.DateTimeField(verbose_name='Discounted expire date')),
                ('is_free', models.BooleanField(default=False, verbose_name='Is Free')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('type', models.CharField(choices=[('course_sale', 'Course sale')], max_length=63, verbose_name='Type')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title_uz', models.CharField(max_length=255, verbose_name='Title_uz')),
                ('title_ru', models.CharField(max_length=255, verbose_name='Title_ru')),
                ('title_en', models.CharField(max_length=255, verbose_name='Title_en')),
                ('icon', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='categories', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rating')),
                ('status', models.CharField(choices=[('accepted', 'accepted'), ('rejected', 'rejected'), ('pending', 'pending'), ('complaint', 'complaint')], max_length=50, verbose_name='Status')),
                ('comment_text', models.TextField(verbose_name='Comment text')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coursecomment_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='course.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Course comment',
                'verbose_name_plural': 'Course comments',
            },
        ),
        migrations.CreateModel(
            name='CourseLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title_uz', models.CharField(max_length=255, verbose_name='Title_uz')),
                ('title_ru', models.CharField(max_length=255, verbose_name='Title_ru')),
                ('title_en', models.CharField(max_length=255, verbose_name='Title_en')),
                ('icon', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='levels', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
            },
        ),
        migrations.CreateModel(
            name='VideoLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('body_text', models.TextField(verbose_name='Body text')),
                ('video_path', models.FileField(upload_to='videos', verbose_name='Video path')),
                ('video_duration', models.DurationField(blank=True, null=True, verbose_name='Video duration')),
                ('video_thumbnail', models.ImageField(upload_to='thumbnails', verbose_name='Video thumbnail')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter', to='course.chapter', verbose_name='Chapter')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='VideoUserViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('viewed_at', models.DateTimeField(auto_now_add=True, verbose_name='Viewed at')),
                ('last_watched_time', models.DurationField(verbose_name='Last Watched Time')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Is Finished')),
                ('progress', models.IntegerField(verbose_name='Progress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_video_views', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_video_views', to='course.videolesson', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Video user view',
                'verbose_name_plural': 'Video user views',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Is Finished')),
                ('finished_at', models.DateTimeField(blank=True, null=True, verbose_name='Finished At')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_courses', to='course.course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_courses', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Course',
                'verbose_name_plural': 'User Courses',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('payment_type', models.CharField(choices=[('uzcard', 'payme'), ('click', 'click'), ('paylov', 'paylov'), ('uzum bank', 'uzum bank')], max_length=50, verbose_name='Payment type')),
                ('payment_status', models.CharField(choices=[('success', 'success'), ('failed', 'failed'), ('pending', 'pending')], max_length=50, verbose_name='Payment status')),
                ('payment_date', models.DateTimeField(verbose_name='Payment date')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_payment', to='course.course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_payment', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='CourseCommentComplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('complaint_type', models.CharField(choices=[('deception', 'deception'), ('offensive', 'offensive'), ('suicide', 'suicide'), ('other', 'other')], max_length=50, verbose_name='Complaint type')),
                ('complaint_text', models.TextField(verbose_name='Complaint text')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='course.coursecomment', verbose_name='Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coursecommentcomplaint_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Course comment complaint',
                'verbose_name_plural': 'Course comment complaints',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='course.coursecategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='course.courselevel', verbose_name='Level'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='course.course', verbose_name='Course'),
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('full_name', models.CharField(max_length=255, null=True, verbose_name='Full Name')),
                ('cid', models.CharField(default=apps.course.utils.randomize_certificate_number, max_length=255, verbose_name='CID')),
                ('file', models.FileField(null=True, upload_to='certificates', verbose_name='File')),
                ('image', models.ImageField(null=True, upload_to='certificates', verbose_name='Image')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='course.course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
                'unique_together': {('user', 'course')},
            },
        ),
    ]
