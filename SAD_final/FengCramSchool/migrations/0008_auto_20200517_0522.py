# Generated by Django 3.0.5 on 2020-05-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FengCramSchool', '0007_auto_20200517_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='in_out',
            field=models.CharField(choices=[('in', 'IN'), ('out', 'OUT')], default='in', max_length=5),
        ),
    ]
