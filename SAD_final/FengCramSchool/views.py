from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentInfo

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django. I don't want to meet you")

def showTemplate(request):
    student_list = StudentInfo.objects.all()
    context = {'student_list': student_list}
    return render(request, 'test.html', context)