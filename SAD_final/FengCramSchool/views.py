from django.shortcuts import render
from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText
import time
import datetime
from .models import Attendance
from .models import CourseSchedule
from .models import Video
from .models import Tuition

from .models import StudentInfo, Scholarship
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return HttpResponse("Hello, Django. I don't want to meet you")


def showTemplate(request):
    student_list = StudentInfo.objects.all()
    context = {'student_list': student_list}
    return render(request, 'test.html', context)


def send_video_URL(request):
    # select當天video的資料
    video_ = list(Video.objects.filter(
        course_date=datetime.date(2020, 5, 17)).values())  # 這邊應該要是today

    # courseID X URL dictionary  這門課的影片連結
    CID_URL = {}
    for i in range(len(video_)):
        if video_[i]["course_schedule_id"] not in CID_URL.keys():
            CID_URL[video_[i]["course_schedule_id"]] = video_[i]["video_url"]

    # courseID X SID dictionary  上這門課的學生有哪些
    CID_SID = {}
    for i in CID_URL.keys():
        CID_SID[i] = []
        cids_sid = list(Tuition.objects.filter(course_schedule_id=i).values())
        for j in range(len(cids_sid)):
            CID_SID[i].append(cids_sid[j]["student_info_id"])

    # 今天有簽到的同學們
    today_arrive = list(Attendance.objects.filter(
        in_out="in", date_time__gt=datetime.date(2020, 5, 17)).values())  # 這邊應該要是today
    today_arr_SID = []
    for i in range(len(today_arrive)):
        today_arr_SID.append(today_arrive[i]["student_info_id"])

    #SID (課的ID,課的URL)
    SID_URL = {}
    for i in CID_SID.keys():
        for j in CID_SID[i]:
            if j not in today_arr_SID:
                if j not in SID_URL:
                    SID_URL[j] = []
                    SID_URL[j].append((i, CID_URL[i]))
                else:
                    SID_URL[j].append((i, CID_URL[i]))

    send_to = []
    for i in SID_URL.keys():
        that_stu_email = list(StudentInfo.objects.filter(id=i).values())[
            0]["email"]
        that_stu_name = list(StudentInfo.objects.filter(id=i).values())[
            0]["student_name"]
        send_class = ""
        for j in range(len(SID_URL[i])):
            real_courseID = list(CourseSchedule.objects.filter(
                id=SID_URL[i][j][0]).values())[0]["courseID"]

            gmail_user = 'superandy0407@gmail.com'
            gmail_password = 'superandy'  # your gmail password

            msg = MIMEText(that_stu_name+'同學你好!\n今天你缺席了(課程ID:' +
                           real_courseID+')這門課\n補課影片連結：'+SID_URL[i][j][1]+'\n請及時補完^^')
            msg['Subject'] = '孔銘數學家教班補課連結'
            msg['From'] = gmail_user
            msg['To'] = that_stu_email

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.send_message(msg)
            server.quit()
            send_class = send_class + " " + real_courseID

#             print('Email sent!')
        send_to.append(that_stu_name + send_class + " " + that_stu_email)
    print(send_to)
    data = {"show": send_to}
    return render(request, 'URLtest.html', data)


@csrf_exempt
def GetScholar(request):
    if request.method == "GET":
        print(request)
        student_list = Scholarship.objects.all()
        for stu in student_list:
            print(stu.student_info)
            print(type(stu.student_info))
        print(student_list)
        context = {'student_list': student_list}
        return render(request, 'scholarship.html', context)
    else:
        print(request.body.decode('ascii').split(","))
        # Modify the real database
        return HttpResponse(request)
