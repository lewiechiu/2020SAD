from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    SID = models.CharField(max_length = 20)
    student_name = models.CharField(max_length = 10)
    birthday = models.DateField()
    school = models.CharField(max_length = 20)
    year = models.DecimalField(max_digits=1, decimal_places=0)
    address = models.CharField(max_length = 50)
    student_phone = models.CharField(max_length = 20)
    parent_name = models.CharField(max_length = 10)
    parent_phone = models.CharField(max_length = 20)
    sibling_name = models.CharField(max_length = 10)
    email = models.CharField(max_length = 30)

    def __str__(self):
        return self.student_name

class Attendance(models.Model):
    SID = models.CharField(max_length = 20)
    date_time = models.DateTimeField()
    in_out = models.BooleanField()

    def __str__(self):
        return self.SID
        
class SchoolRecord(models.Model):
    SID = models.CharField(max_length = 20)
    category = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 20) #可改成選項
    record_url = models.URLField
    grade = models.CharField(max_length = 20)
    scholarshipID = models.CharField(max_length = 20)

    def __str__(self):
        return self.SID

class CramRecord(models.Model):
    SID = models.CharField(max_length = 20)
    quizID = models.CharField(max_length = 20)
    quiz_grade = models.CharField(max_length = 20)

    def __str__(self):
        return self.SID

class Quiz(models.Model):
    quizID = models.CharField(max_length = 20)
    quiz_date = models.DateField()
    quiz_description = models.CharField(max_length = 20)

    def __str__(self):
        return self.quizID

class CourseSchedule(models.Model):
    courseID = models.CharField(max_length = 20)
    course = models.CharField(max_length = 20)
    class_time = models.TimeField

    def __str__(self):
        return self.courseID


class Tuition(models.Model):
    SID = models.CharField(max_length = 20)
    received_date = models.DateField
    courseID = models.CharField(max_length = 20)
    tuition_payment = models.CharField(max_length = 10)

    def __str__(self):
        return self.SID

class Scholarship(models.Model):
    SID = models.CharField(max_length = 20)
    scholarshipID = models.CharField(max_length = 20)
    payment_date = models.DateField
    scholarship_description = models.CharField(max_length = 20)
    scholarship_payment = models.CharField(max_length = 10)

    def __str__(self):
        return self.SID

class Video(models.Model):
    VID = models.CharField(max_length = 20)
    courseID = models.CharField(max_length = 20)
    video_url = models.URLField
    course_date = models.DateField
    
    def __str__(self):
        return self.VID
