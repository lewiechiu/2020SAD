from django.contrib import admin

from .models import StudentInfo, Attendance

# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(Attendance)


