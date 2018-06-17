from django.http import HttpResponse
from ..data.login_data import login_data
from ..data.Course import Course
import time

def login(request):
    account=request.GET.get("account")
    password=request.GET.get("password")
    return HttpResponse(login_data(account,password))
    pass

def addCourse(request):
    course=Course()
    cid="a"+str(time.strftime("%H%M%S"))
    cnm=request.POST.get("cnm")
    credit=request.POST.get("credit")
    teacher=request.POST.get("teacher")
    croom=request.POST.get("room")
    share=request.POST.get("share")
    return HttpResponse(course.addCourse(cid,cnm,credit,teacher,croom,share))
    pass

def removeCourse(request):
    course=Course()
    cid=request.GET.get("cid")
    return HttpResponse(course.removeCourse(cid))
    pass