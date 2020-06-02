from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    SID = models.CharField('學生編號', max_length = 20)
    student_name = models.CharField('學生姓名', max_length = 30)
    birthday = models.DateField('生日', blank=True, null = True)
    school = models.CharField('學校', max_length = 50, blank=True, null = True)
    year = models.DecimalField('年級', max_digits=2, decimal_places=0, blank=True, null = True)
    address = models.CharField('地址', max_length = 100, blank=True, null = True)
    student_phone = models.CharField('學生電話', max_length = 20, blank=True, null = True)
    parent_name = models.CharField('家長姓名', max_length = 30, blank=True, null = True)
    parent_phone = models.CharField('家長電話', max_length = 20, blank=True, null = True)
    sibling_name = models.CharField('兄弟姐妹姓名', max_length = 30, blank=True, null = True)
    email = models.CharField('電子郵件', max_length = 50, blank=True, null = True)

    def __str__(self):
        return self.student_name
    
    class Meta:
        verbose_name = '學生資料'
        verbose_name_plural = '學生資料'

class Attendance(models.Model):
    # SID = models.CharField(max_length = 20)
    student_info = models.ForeignKey(
        StudentInfo,
        related_name = 'attendance_student_info',
        on_delete = models.CASCADE,
        default = 1
    )
    date_time = models.DateTimeField('時間', blank=True, null = True)
    IN_OUT_CHOICES = (
        ('in', '進班'),
        ('out', '出班')
    )
    # in_out = models.NullBooleanField(blank=True, null = True)
    in_out = models.CharField('進班/出班', max_length = 5, choices = IN_OUT_CHOICES, default = 'in', blank=True, null = True)

    def __str__(self):
        return self.student_info.student_name + '_' + str(self.date_time)

    class Meta:
        verbose_name = '出缺席紀錄'
        verbose_name_plural = '出缺席紀錄'

class CourseSchedule(models.Model):
    courseID = models.CharField('課程編號', max_length = 20)
    course = models.CharField('課程名稱', max_length = 50, blank=True, null = True)
    class_time = models.TimeField('課程時間', blank=True, null = True)
    TYPES_CHOICES = (
        ('rank', '名次'),
        ('score', '分數')
    )
    scholarship_type = models.CharField('獎學金標準類別', max_length = 20, choices = TYPES_CHOICES, default = 'score', blank = True, null = True)
    scholarship_value = models.DecimalField('獎學金領取標準', max_digits=4, decimal_places=1, default = 90.0, blank=True, null = True)
    scholarship_amount = models.DecimalField('獎學金金額', max_digits=6, decimal_places=1, default = 200.0, blank=True, null = True)

    def __str__(self):
        return self.courseID + '_' + self.course

    class Meta:
        verbose_name = '課程表'
        verbose_name_plural = '課程表'

class SchoolRecord(models.Model):
    # SID = models.CharField(max_length = 20)
    student_info = models.ForeignKey(
        StudentInfo,
        related_name = 'schoolRecord_student_info',
        on_delete = models.CASCADE,
        default = 1
    )
    category = models.CharField('考試類別', max_length = 50, blank=True, null = True)
    SUBJECT_CHOICES = (
        ('math', '數學'),
        ('english', '英文'),
        ('chinese', '國文')
    )
    subject = models.CharField('科目', max_length = 20, choices = SUBJECT_CHOICES, default= 'math', blank=True, null = True)
    record_url = models.URLField('成績單連結', blank=True, null = True)
    grade = models.DecimalField('分數', max_digits=4, decimal_places=1, blank=True, null = True)
    rank = models.DecimalField('名次', max_digits=4, decimal_places=1, blank=True, null = True)
    related_course = models.ForeignKey(
        CourseSchedule,
        related_name = 'schoolRecord_related_course',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    def __str__(self):
        if self.grade != None:
            return self.student_info.student_name + self.category + "_" + str(self.grade)
        else:
            return self.student_info.student_name + self.category + "_" + str(int(self.rank))

    class Meta:
        verbose_name = '在校成績紀錄'
        verbose_name_plural = '在校成績紀錄'

class Quiz(models.Model):
    quizID = models.CharField('小考編號', max_length = 20)
    quiz_date = models.DateField('小考日期', blank=True, null = True)
    quiz_description = models.CharField('小考內容', max_length = 100, blank=True, null = True)

    def __str__(self):
        return self.quizID

    class Meta:
        verbose_name = '補習班小考資訊'
        verbose_name_plural = '補習班小考資訊'

class CramRecord(models.Model):
    # SID = models.CharField(max_length = 20)
    student_info = models.ForeignKey(
        StudentInfo,
        related_name = 'cramRecord_student_info',
        on_delete = models.CASCADE,
        default = 1
    )
    # quizID = models.CharField(max_length = 20, blank=True, null = True)
    quiz = models.ForeignKey(
        Quiz,
        related_name = 'cramRecord_quiz',
        on_delete = models.CASCADE,
        default = 1
    )
    quiz_grade = models.DecimalField('小考成績', max_digits=4, decimal_places=1, blank=True, null = True)

    def __str__(self):
        return self.student_info.student_name + '_' + self.quiz.quizID

    class Meta:
        verbose_name = '補習班小考成績紀錄'
        verbose_name_plural = '補習班小考成績紀錄'

class Tuition(models.Model):
    # SID = models.CharField(max_length = 20)
    student_info = models.ForeignKey(
        StudentInfo,
        related_name = 'tuition_student_info',
        on_delete = models.CASCADE,
        default = 1
    )
    received_date = models.DateField('收款日期', blank=True, null = True)
    # courseID = models.CharField(max_length = 20, blank=True, null = True)
    course_schedule = models.ForeignKey(
        CourseSchedule,
        related_name = 'tuition_course_schedule',
        on_delete = models.CASCADE,
        default = 1
    )
    tuition_payment = models.DecimalField('收款金額', max_digits=6, decimal_places=1, blank=True, null = True)
    
    def __str__(self):
        return self.student_info.student_name + '_' + self.course_schedule.courseID

    class Meta:
        verbose_name = '學生繳費記錄'
        verbose_name_plural = '學生繳費記錄'

class Scholarship(models.Model):
    # SID = models.CharField(max_length = 20)
    student_info = models.ForeignKey(
        StudentInfo,
        related_name = 'scholarship_student_info',
        on_delete = models.CASCADE,
        default = 1
    )
    school_record = models.ForeignKey(
        SchoolRecord,
        related_name = 'scholarship_school_record',
        on_delete = models.CASCADE,
        default = 1
    )
    # scholarshipID = models.CharField(max_length = 20, blank = True, null = True)
    payment_date = models.DateField('頒發日期', blank=True, null = True)
    scholarship_description = models.CharField('頒發理由', max_length = 100, blank=True, null = True)
    scholarship_payment = models.DecimalField('獎學金金額', max_digits=6, decimal_places=1, blank=True, null = True)
    STATUS = (
        ('paid', '已頒發'),
        ('unpaid', '未頒發')
    )
    status = models.CharField('獎學金頒發狀態', max_length = 20, choices = STATUS, default = 'unpaid', blank = True, null = True)

    def __str__(self):
        return self.student_info.student_name 

    class Meta:
        verbose_name = '獎學金紀錄'
        verbose_name_plural = '獎學金紀錄'

class Video(models.Model):
    VID = models.CharField('課程影片編號', max_length = 20)
    # courseID = models.CharField(max_length = 20, blank=True, null = True)
    course_schedule = models.ForeignKey(
        CourseSchedule,
        related_name = 'video_course_schedule',
        on_delete = models.CASCADE,
        default = 1
    )
    video_url = models.URLField('課程影片連結', blank=True, null = True)
    course_date = models.DateField('課程日期', blank=True, null = True)
    
    def __str__(self):
        return self.VID

    class Meta:
        verbose_name = '課程影片連結'
        verbose_name_plural = '課程影片連結'