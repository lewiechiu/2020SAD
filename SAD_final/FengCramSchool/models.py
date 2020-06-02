from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    SID = models.CharField(max_length = 20)
    student_name = models.CharField(max_length = 30)
    birthday = models.DateField(blank=True, null = True)
    school = models.CharField(max_length = 50, blank=True, null = True)
    year = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null = True)
    address = models.CharField(max_length = 100, blank=True, null = True)
    student_phone = models.CharField(max_length = 20, blank=True, null = True)
    parent_name = models.CharField(max_length = 30, blank=True, null = True)
    parent_phone = models.CharField(max_length = 20, blank=True, null = True)
    sibling_name = models.CharField(max_length = 30, blank=True, null = True)
    email = models.CharField(max_length = 50, blank=True, null = True)

    def __str__(self):
        return self.student_name
    
    class Meta:
        verbose_name_plural = '學生資料'

class Attendance(models.Model):
    # SID = models.CharField(max_length = 20)
    student_info = models.ForeignKey(
        StudentInfo,
        related_name = 'attendance_student_info',
        on_delete = models.CASCADE,
        default = 1
    )
    date_time = models.DateTimeField(blank=True, null = True)
    IN_OUT_CHOICES = (
        ('in', 'IN'),
        ('out', 'OUT')
    )
    # in_out = models.NullBooleanField(blank=True, null = True)
    in_out = models.CharField(max_length = 5, choices = IN_OUT_CHOICES, default = 'in', blank=True, null = True)

    def __str__(self):
        return self.student_info.student_name + '_' + str(self.date_time)
        
class SchoolRecord(models.Model):
    # SID = models.CharField(max_length = 20)
    student_info = models.ForeignKey(
        StudentInfo,
        related_name = 'schoolRecord_student_info',
        on_delete = models.CASCADE,
        default = 1
    )
    category = models.CharField(max_length = 50, blank=True, null = True)
    SUBJECT_CHOICES = (
        ('math', 'Math'),
        ('english', 'English'),
        ('chinese', 'Chinese')
    )
    subject = models.CharField(max_length = 20, choices = SUBJECT_CHOICES, default= 'math', blank=True, null = True)
    record_url = models.URLField(blank=True, null = True)
    grade = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null = True)
    scholarshipID = models.CharField(max_length = 20, blank=True, null = True)

    def __str__(self):
        return self.student_info.student_name + '_' + self.scholarshipID

class Quiz(models.Model):
    quizID = models.CharField(max_length = 20)
    quiz_date = models.DateField(blank=True, null = True)
    quiz_description = models.CharField(max_length = 100, blank=True, null = True)

    def __str__(self):
        return self.quizID

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
    quiz_grade = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null = True)

    def __str__(self):
        return self.student_info.student_name + '_' + self.quiz.quizID

class CourseSchedule(models.Model):
    courseID = models.CharField(max_length = 20)
    course = models.CharField(max_length = 50, blank=True, null = True)
    class_time = models.TimeField(blank=True, null = True)

    def __str__(self):
        return self.courseID + '_' + self.course


class Tuition(models.Model):
    # SID = models.CharField(max_length = 20)
    student_info = models.ForeignKey(
        StudentInfo,
        related_name = 'tuition_student_info',
        on_delete = models.CASCADE,
        default = 1
    )
    received_date = models.DateField(blank=True, null = True)
    # courseID = models.CharField(max_length = 20, blank=True, null = True)
    course_schedule = models.ForeignKey(
        CourseSchedule,
        related_name = 'tuition_course_schedule',
        on_delete = models.CASCADE,
        default = 1
    )
    tuition_payment = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null = True)
    
    def __str__(self):
        return self.student_info.student_name + '_' + self.course_schedule.courseID

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
    payment_date = models.DateField(blank=True, null = True)
    scholarship_description = models.CharField(max_length = 100, blank=True, null = True)
    scholarship_payment = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null = True)

    def __str__(self):
        return self.student_info.student_name + '_' + self.school_record.scholarshipID

class Video(models.Model):
    VID = models.CharField(max_length = 20)
    # courseID = models.CharField(max_length = 20, blank=True, null = True)
    course_schedule = models.ForeignKey(
        CourseSchedule,
        related_name = 'video_course_schedule',
        on_delete = models.CASCADE,
        default = 1
    )
    video_url = models.URLField(blank=True, null = True)
    course_date = models.DateField(blank=True, null = True)
    
    def __str__(self):
        return self.VID