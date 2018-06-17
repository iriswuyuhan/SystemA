import xml.dom.minidom as dm

from django.http import HttpResponse

from ..data.Course import Course

import urllib.parse
import urllib.request

from .constants import host

def getSelect(request):
    sid=str(request.GET.get("sid"))
    course = Course()
    courseInfo = course.getCourse()
    stuCourseInfo = course.getSelectCourse(sid)
    for i in range(0,len(courseInfo)):
        courseInfo[i]=list(courseInfo[i])
        courseInfo[i].append(False)
    for i in range(0,len(stuCourseInfo)):
        cid=int(stuCourseInfo[i][0][1:])
        courseInfo[cid][6]=True

    doc = dm.Document()
    root = doc.createElementNS("nju.edu.cn/schema/a", "a:课程列表")
    attr = doc.createAttribute("xmlns:a")
    attr.value = "nju.edu.cn/schema/a"
    root.setAttributeNode(attr)
    for item in courseInfo:
        c = doc.createElement("a:课程")
        cid = doc.createElement("a:课程编号")
        cid.appendChild(doc.createTextNode(item[0]))
        c.appendChild(cid)
        cnm = doc.createElement("a:课程名称")
        cnm.appendChild(doc.createTextNode(item[1]))
        c.appendChild(cnm)
        credit = doc.createElement("a:学分")
        credit.appendChild(doc.createTextNode(item[2]))
        c.appendChild(credit)
        tnm = doc.createElement("a:授课老师")
        tnm.appendChild(doc.createTextNode(item[3]))
        c.appendChild(tnm)
        croom = doc.createElement("a:授课地点")
        croom.appendChild(doc.createTextNode(item[4]))
        c.appendChild(croom)
        share = doc.createElement("a:共享")
        share.appendChild(doc.createTextNode(item[5]))
        c.appendChild(share)
        select=doc.createElement("a:选择")
        select.appendChild(doc.createTextNode(str(item[6])))
        c.appendChild(select)
        root.appendChild(c)

    # text={'sid':sid}
    # text=urllib.parse.urlencode(text)
    # url=host
    # req=urllib.request.Request(url='%s%s%s' % (url,'?',text))
    # res=urllib.request.urlopen(req)
    # content=res.read()
    #
    # bodydata = content.body
    # doc = dm.parseString(bodydata.decode("utf-8"))
    doc.appendChild(root)
    return HttpResponse(doc.toxml(),"text/xml")

def getAllSelect(request):
    course=Course()
    courseInfo=course.getAllSelect()
    wrapped=wrapSelect(courseInfo)
    return HttpResponse(wrapped,"text/xml")

def wrapSelect(courseInfo):
    doc = dm.Document()
    root = doc.createElementNS("nju.edu.cn/schema/a", "a:选课列表")
    attr = doc.createAttribute("xmlns:a")
    attr.value = "nju.edu.cn/schema/a"
    root.setAttributeNode(attr)
    for item in courseInfo:
        select = doc.createElement("a:选课")
        dep = doc.createElement("a:开课院系")
        dep.appendChild(doc.createTextNode("A"))
        select.appendChild(dep)
        sid = doc.createElement("a:学号")
        sid.appendChild(doc.createTextNode(item[1]))
        select.appendChild(sid)
        cid = doc.createElement("a:课程编号")
        cid.appendChild(doc.createTextNode(item[0]))
        select.appendChild(cid)
        grd = doc.createElement("a:成绩")
        grd.appendChild(doc.createTextNode("无"))
        select.appendChild(grd)
        root.appendChild(select)
    doc.appendChild(root)
    return doc.toxml()

def getAll(request):
    course = Course()
    courseInfo = course.getCourse()
    doc = dm.Document()
    root = doc.createElementNS("nju.edu.cn/schema/a", "a:课程列表")
    attr = doc.createAttribute("xmlns:a")
    attr.value = "nju.edu.cn/schema/a"
    root.setAttributeNode(attr)
    for item in courseInfo:
        c = doc.createElement("a:课程")
        cid = doc.createElement("a:课程编号")
        cid.appendChild(doc.createTextNode(item[0]))
        c.appendChild(cid)
        cnm = doc.createElement("a:课程名称")
        cnm.appendChild(doc.createTextNode(item[1]))
        c.appendChild(cnm)
        credit = doc.createElement("a:学分")
        credit.appendChild(doc.createTextNode(item[2]))
        c.appendChild(credit)
        tnm = doc.createElement("a:授课老师")
        tnm.appendChild(doc.createTextNode(item[3]))
        c.appendChild(tnm)
        croom = doc.createElement("a:授课地点")
        croom.appendChild(doc.createTextNode(item[4]))
        c.appendChild(croom)
        share = doc.createElement("a:共享")
        share.appendChild(doc.createTextNode(item[5]))
        c.appendChild(share)
        root.appendChild(c)
    doc.appendChild(root)
    return HttpResponse(doc.toxml(),"text/xml")

def getStu(request):
    sid = str(request.GET.get("sid"))
    course = Course()
    stuCourseInfo = course.getSelectCourse(sid)
    wrapped=wrapSelect(stuCourseInfo)
    return HttpResponse(wrapped,"text/xml")

def checkSelect(request):
    sid=str(request.GET.get("sid"))
    cid=str(request.GET.get("cid"))
    course=Course()
    return HttpResponse(course.checkCourse(sid,cid))

def getStatistic(request):
    course=Course()
    courseInfo=course.getCourse()
    courseSelect=course.getAllSelect()
    select=[]

    for i in range(0,len(courseSelect)):
        select.append(courseSelect[i][0])

    for i in range(0,len(courseInfo)):
        cid=courseInfo[i][0]
        countNum=select.count(cid)
        courseInfo[i]=list(courseInfo[i])
        courseInfo[i].append(countNum)

    doc = dm.Document()
    root = doc.createElementNS("nju.edu.cn/schema/a", "a:课程选课统计列表")
    attr = doc.createAttribute("xmlns:a")
    attr.value = "nju.edu.cn/schema/a"
    root.setAttributeNode(attr)
    for item in courseInfo:
        info=doc.createElement("a:课程选课统计")
        c = doc.createElement("a:课程")
        cid = doc.createElement("a:课程编号")
        cid.appendChild(doc.createTextNode(item[0]))
        c.appendChild(cid)
        cnm = doc.createElement("a:课程名称")
        cnm.appendChild(doc.createTextNode(item[1]))
        c.appendChild(cnm)
        credit = doc.createElement("a:学分")
        credit.appendChild(doc.createTextNode(item[2]))
        c.appendChild(credit)
        tnm = doc.createElement("a:授课老师")
        tnm.appendChild(doc.createTextNode(item[3]))
        c.appendChild(tnm)
        croom = doc.createElement("a:授课地点")
        croom.appendChild(doc.createTextNode(item[4]))
        c.appendChild(croom)
        share = doc.createElement("a:共享")
        share.appendChild(doc.createTextNode(item[5]))
        c.appendChild(share)
        num=doc.createElement("a:选课人数")
        num.appendChild(doc.createTextNode(str(item[6])))
        info.appendChild(c)
        info.appendChild(num)
        root.appendChild(info)
    doc.appendChild(root)

    return HttpResponse(doc.toxml(),"text/xml")

def getShare(request):
    sid = str(request.GET.get("sid"))
    course = Course()
    courseInfo = course.getCourse()
    stuCourseInfo = course.getSelectCourse(sid)
    for i in range(0, len(courseInfo)):
        courseInfo[i] = list(courseInfo[i])
        courseInfo[i].append(False)
    for i in range(0, len(stuCourseInfo)):
        cid = int(stuCourseInfo[i][0][1:])
        courseInfo[cid][6] = True

    doc = dm.Document()
    root = doc.createElementNS("nju.edu.cn/schema/a", "a:课程列表")
    attr = doc.createAttribute("xmlns:a")
    attr.value = "nju.edu.cn/schema/a"
    root.setAttributeNode(attr)
    for item in courseInfo:
        if item[5]=='Y':
            c = doc.createElement("a:课程")
            cid = doc.createElement("a:课程编号")
            cid.appendChild(doc.createTextNode(item[0]))
            c.appendChild(cid)
            cnm = doc.createElement("a:课程名称")
            cnm.appendChild(doc.createTextNode(item[1]))
            c.appendChild(cnm)
            credit = doc.createElement("a:学分")
            credit.appendChild(doc.createTextNode(item[2]))
            c.appendChild(credit)
            tnm = doc.createElement("a:授课老师")
            tnm.appendChild(doc.createTextNode(item[3]))
            c.appendChild(tnm)
            croom = doc.createElement("a:授课地点")
            croom.appendChild(doc.createTextNode(item[4]))
            c.appendChild(croom)
            share = doc.createElement("a:共享")
            share.appendChild(doc.createTextNode(item[5]))
            c.appendChild(share)
            select = doc.createElement("a:选择")
            select.appendChild(doc.createTextNode(str(item[6])))
            c.appendChild(select)
            root.appendChild(c)
    doc.appendChild(root)
    return HttpResponse(doc.toxml(), "text/xml")
    pass

def getCross(request):
    sid = request.GET.get("sid")
    dep = request.GET.get("dep")
    system='a'

    text = {'sid': sid, 'dep': dep,'system':system}
    text = urllib.parse.urlencode(text)
    url = host+"api/getUserShareCourses"
    req = urllib.request.Request(url='%s%s%s' % (url, '?', text))
    res = urllib.request.urlopen(req)
    content = res.read()
    print(content.decode("utf-8"))

    doc = dm.parseString(content.decode("utf-8"))

    return HttpResponse(doc.toxml(), "text/xml")
    pass