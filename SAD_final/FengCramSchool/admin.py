from django.contrib import admin

from .models import StudentInfo, Attendance, SchoolRecord,CramRecord, Quiz, CourseSchedule, Tuition, Scholarship, Video

# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(Attendance)
admin.site.register(SchoolRecord)
admin.site.register(CramRecord)
admin.site.register(Quiz)
admin.site.register(CourseSchedule)
admin.site.register(Tuition)
admin.site.register(Scholarship)
admin.site.register(Video)


