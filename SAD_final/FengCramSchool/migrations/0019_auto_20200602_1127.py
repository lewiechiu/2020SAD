# Generated by Django 3.0.5 on 2020-06-02 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FengCramSchool', '0018_auto_20200517_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name': '出缺席紀錄', 'verbose_name_plural': '出缺席紀錄'},
        ),
        migrations.AlterModelOptions(
            name='courseschedule',
            options={'verbose_name': '課程表', 'verbose_name_plural': '課程表'},
        ),
        migrations.AlterModelOptions(
            name='cramrecord',
            options={'verbose_name': '補習班小考成績紀錄', 'verbose_name_plural': '補習班小考成績紀錄'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': '補習班小考資訊', 'verbose_name_plural': '補習班小考資訊'},
        ),
        migrations.AlterModelOptions(
            name='scholarship',
            options={'verbose_name': '獎學金紀錄', 'verbose_name_plural': '獎學金紀錄'},
        ),
        migrations.AlterModelOptions(
            name='schoolrecord',
            options={'verbose_name': '在校成績紀錄', 'verbose_name_plural': '在校成績紀錄'},
        ),
        migrations.AlterModelOptions(
            name='studentinfo',
            options={'verbose_name': '學生資料', 'verbose_name_plural': '學生資料'},
        ),
        migrations.AlterModelOptions(
            name='tuition',
            options={'verbose_name': '學生繳費記錄', 'verbose_name_plural': '學生繳費記錄'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': '課程影片連結', 'verbose_name_plural': '課程影片連結'},
        ),
        migrations.AddField(
            model_name='courseschedule',
            name='scholarship_amount',
            field=models.DecimalField(blank=True, decimal_places=1, default=200.0, max_digits=6, null=True, verbose_name='獎學金金額'),
        ),
        migrations.AddField(
            model_name='courseschedule',
            name='scholarship_type',
            field=models.CharField(blank=True, choices=[('rank', '名次'), ('score', '分數')], default='score', max_length=20, null=True, verbose_name='獎學金標準類別'),
        ),
        migrations.AddField(
            model_name='courseschedule',
            name='scholarship_value',
            field=models.DecimalField(blank=True, decimal_places=1, default=90.0, max_digits=4, null=True, verbose_name='獎學金領取標準'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='status',
            field=models.CharField(blank=True, choices=[('paid', '已頒發'), ('unpaid', '未頒發')], default='unpaid', max_length=20, null=True, verbose_name='獎學金頒發狀態'),
        ),
        migrations.AddField(
            model_name='schoolrecord',
            name='rank',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='名次'),
        ),
        migrations.AddField(
            model_name='schoolrecord',
            name='related_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schoolRecord_related_course', to='FengCramSchool.CourseSchedule'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='時間'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='in_out',
            field=models.CharField(blank=True, choices=[('in', '進班'), ('out', '出班')], default='in', max_length=5, null=True, verbose_name='進班/出班'),
        ),
        migrations.AlterField(
            model_name='courseschedule',
            name='class_time',
            field=models.TimeField(blank=True, null=True, verbose_name='課程時間'),
        ),
        migrations.AlterField(
            model_name='courseschedule',
            name='course',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='課程名稱'),
        ),
        migrations.AlterField(
            model_name='courseschedule',
            name='courseID',
            field=models.CharField(max_length=20, verbose_name='課程編號'),
        ),
        migrations.AlterField(
            model_name='cramrecord',
            name='quiz_grade',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='小考成績'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='quizID',
            field=models.CharField(max_length=20, verbose_name='小考編號'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='quiz_date',
            field=models.DateField(blank=True, null=True, verbose_name='小考日期'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='quiz_description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='小考內容'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='頒發日期'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='scholarship_description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='頒發理由'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='scholarship_payment',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, verbose_name='獎學金金額'),
        ),
        migrations.AlterField(
            model_name='schoolrecord',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='考試類別'),
        ),
        migrations.AlterField(
            model_name='schoolrecord',
            name='grade',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='分數'),
        ),
        migrations.AlterField(
            model_name='schoolrecord',
            name='record_url',
            field=models.URLField(blank=True, null=True, verbose_name='成績單連結'),
        ),
        migrations.AlterField(
            model_name='schoolrecord',
            name='scholarshipID',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='獎學金編號'),
        ),
        migrations.AlterField(
            model_name='schoolrecord',
            name='subject',
            field=models.CharField(blank=True, choices=[('math', '數學'), ('english', '英文'), ('chinese', '國文')], default='math', max_length=20, null=True, verbose_name='科目'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='SID',
            field=models.CharField(max_length=20, verbose_name='學生編號'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='電子郵件'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='parent_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='家長姓名'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='parent_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='家長電話'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='school',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='學校'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='sibling_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='兄弟姐妹姓名'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='student_name',
            field=models.CharField(max_length=30, verbose_name='學生姓名'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='student_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='學生電話'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='year',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, verbose_name='年級'),
        ),
        migrations.AlterField(
            model_name='tuition',
            name='received_date',
            field=models.DateField(blank=True, null=True, verbose_name='收款日期'),
        ),
        migrations.AlterField(
            model_name='tuition',
            name='tuition_payment',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, verbose_name='收款金額'),
        ),
        migrations.AlterField(
            model_name='video',
            name='VID',
            field=models.CharField(max_length=20, verbose_name='課程影片編號'),
        ),
        migrations.AlterField(
            model_name='video',
            name='course_date',
            field=models.DateField(blank=True, null=True, verbose_name='課程日期'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.URLField(blank=True, null=True, verbose_name='課程影片連結'),
        ),
    ]
