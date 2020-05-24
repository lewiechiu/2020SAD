from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentInfo, Scholarship
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return HttpResponse("Hello, Django. I don't want to meet you")

def showTemplate(request):
    student_list = StudentInfo.objects.all()
    context = {'student_list': student_list}
    return render(request, 'test.html', context)

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
    