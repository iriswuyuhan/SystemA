from django.http import HttpResponse
from ..data.Course import Course
import urllib.parse
import urllib.request

from .constants import host

def drop(request):
    sid = str(request.GET.get('sid'))
    cid = str(request.GET.get('cid'))
    success=False
    if cid[0]=='a':
        course=Course()
        success=course.dropCourse(sid,cid)
    else:
        text = {'sId': sid, 'cId': cid}
        text = urllib.parse.urlencode(text)
        url = host+"api/quitCourse"
        req = urllib.request.Request(url='%s%s%s' % (url, '?', text))
        res = urllib.request.urlopen(req)
        success = res.read()
    return HttpResponse(success)
