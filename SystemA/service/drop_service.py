from django.http import HttpResponse
from ..data.Course import Course

def drop(request):
    sid = str(request.GET.get('sid'))
    cid = str(request.GET.get('cid'))
    course=Course()
    if course.dropCourse(sid,cid):
        return HttpResponse(True)
    else:
        return HttpResponse(False)