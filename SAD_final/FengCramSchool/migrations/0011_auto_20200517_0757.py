# Generated by Django 3.0.5 on 2020-05-17 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FengCramSchool', '0010_auto_20200517_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='scholarshipID',
            field=models.CharField(max_length=20),
        ),
    ]
