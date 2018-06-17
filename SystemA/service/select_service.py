from django.http import HttpResponse
from ..data.Course import Course
import urllib.parse
import urllib.request

from .constants import host

def select(request):
    sid=str(request.GET.get('sid'))
    cid=str(request.GET.get('cid'))
    print(sid)
    print(cid)
    success=False
    if cid[0]=='a':
        course=Course()
        success=course.selectCourse(sid,cid)
    else:
        text = {'sId': sid, 'cId': cid}
        text = urllib.parse.urlencode(text)
        url = host+"api/chooseCourse"
        req = urllib.request.Request(url='%s%s%s' % (url, '?', text))
        res = urllib.request.urlopen(req)
        success = res.read()
    return HttpResponse(success)