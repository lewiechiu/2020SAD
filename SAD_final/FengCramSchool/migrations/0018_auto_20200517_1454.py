# Generated by Django 3.0.5 on 2020-05-17 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FengCramSchool', '0017_auto_20200517_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='courseID',
        ),
        migrations.AddField(
            model_name='video',
            name='course_schedule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='video_course_schedule', to='FengCramSchool.CourseSchedule'),
        ),
    ]
