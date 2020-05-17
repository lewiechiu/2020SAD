from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    SID = models.CharField(max_length = 20)
    student_name = models.CharField(max_length = 10)
    birthday = models.DateField(blank=True, null = True)
    school = models.CharField(max_length = 20, blank=True, null = True)
    year = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null = True)
    address = models.CharField(max_length = 50, blank=True, null = True)
    student_phone = models.CharField(max_length = 20, blank=True, null = True)
    parent_name = models.CharField(max_length = 10, blank=True, null = True)
    parent_phone = models.CharField(max_length = 20, blank=True, null = True)
    sibling_name = models.CharField(max_length = 10, blank=True, null = True)
    email = models.CharField(max_length = 30, blank=True, null = True)

    def __str__(self):
        return self.student_name

class Attendance(models.Model):
    SID = models.CharField(max_length = 20)
    date_time = models.DateTimeField(blank=True, null = True)
    IN_OUT_CHOICES = (
        ('in', 'IN'),
        ('out', 'OUT')
    )
    # in_out = models.NullBooleanField(blank=True, null = True)
    in_out = models.CharField(max_length = 5, choices = IN_OUT_CHOICES, default = 'in', blank=True, null = True)

    def __str__(self):
        return self.SID
        
class SchoolRecord(models.Model):
    SID = models.CharField(max_length = 20)
    category = models.CharField(max_length = 20, blank=True, null = True)
    SUBJECT_CHOICES = (
        ('math', 'Math'),
        ('english', 'English'),
        ('chinese', 'Chinese')
    )
    subject = models.CharField(max_length = 20, choices = SUBJECT_CHOICES, default= 'math', blank=True, null = True)
    record_url = models.URLField(blank=True, null = True)
    grade = models.CharField(max_length = 20, blank=True, null = True)
    scholarshipID = models.CharField(max_length = 20, blank=True, null = True)

    def __str__(self):
        return self.SID

class CramRecord(models.Model):
    SID = models.CharField(max_length = 20)
    quizID = models.CharField(max_length = 20, blank=True, null = True)
    quiz_grade = models.CharField(max_length = 20, blank=True, null = True)

    def __str__(self):
        return self.SID

class Quiz(models.Model):
    quizID = models.CharField(max_length = 20)
    quiz_date = models.DateField(blank=True, null = True)
    quiz_description = models.CharField(max_length = 20, blank=True, null = True)

    def __str__(self):
        return self.quizID

class CourseSchedule(models.Model):
    courseID = models.CharField(max_length = 20)
    course = models.CharField(max_length = 20, blank=True, null = True)
    class_time = models.TimeField(blank=True, null = True)

    def __str__(self):
        return self.courseID


class Tuition(models.Model):
    SID = models.CharField(max_length = 20)
    received_date = models.DateField(blank=True, null = True)
    courseID = models.CharField(max_length = 20, blank=True, null = True)
    tuition_payment = models.CharField(max_length = 10, blank=True, null = True)

    def __str__(self):
        return self.SID

class Scholarship(models.Model):
    SID = models.CharField(max_length = 20)
    scholarshipID = models.CharField(max_length = 20, blank=True, null = True)
    payment_date = models.DateField(blank=True, null = True)
    scholarship_description = models.CharField(max_length = 20, blank=True, null = True)
    scholarship_payment = models.CharField(max_length = 10, blank=True, null = True)

    def __str__(self):
        return self.SID

class Video(models.Model):
    VID = models.CharField(max_length = 20)
    courseID = models.CharField(max_length = 20, blank=True, null = True)
    video_url = models.URLField(blank=True, null = True)
    course_date = models.DateField(blank=True, null = True)
    
    def __str__(self):
        return self.VID
