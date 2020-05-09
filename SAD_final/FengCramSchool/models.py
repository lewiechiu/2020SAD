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
    parent = models.CharField(max_length = 10)
    parent_phone = models.CharField(max_length = 20)
    sibling_name = models.CharField(max_length = 10)
    email = models.CharField(max_length = 30)

    def __str__(self):
        return self.student_name

class Attendence(models.Model):
    SID = models.CharField(max_length = 20)
    date_time = models.DateTimeField()
    in_out = models.BooleanField()

    def __str__(self):
        return self.SID
        