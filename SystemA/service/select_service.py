from django.http import HttpResponse
from ..data.Course import Course

def select(request):
    sid=str(request.GET.get('sid'))
    cid=str(request.GET.get('cid'))
    print(sid)
    print(cid)
    course=Course()
    if course.selectCourse(sid,cid):
        return HttpResponse(True)
    else:
        return HttpResponse(False)