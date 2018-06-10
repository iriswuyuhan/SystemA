from django.http import HttpResponse
from ..data.Course import Course
import xml.dom.minidom as dm

def getSelect(request):
    sid=str(request.GET.get("sid"))
    course = Course()
    courseInfo = course.getSelectCourse(sid)
    wrapped=wrapSelect(courseInfo)
    return HttpResponse(wrapped,"text/xml")

def getAllSelect(request):
    course=Course()
    courseInfo=course.getAllSelect()
    wrapped=wrapSelect(courseInfo)
    return HttpResponse(wrapped,"text/xml")

def wrapSelect(courseInfo):
    doc = dm.Document()
    root = doc.createElement("选课列表")
    for item in courseInfo:
        select = doc.createElement("选课")
        dep = doc.createElement("开课院系")
        dep.appendChild(doc.createTextNode("A"))
        select.appendChild(dep)
        sid = doc.createElement("学号")
        sid.appendChild(doc.createTextNode(item[1]))
        select.appendChild(sid)
        cid = doc.createElement("课程编号")
        cid.appendChild(doc.createTextNode(item[0]))
        select.appendChild(cid)
        grd = doc.createElement("成绩")
        grd.appendChild(doc.createTextNode(item[2]))
        select.appendChild(grd)
        root.appendChild(select)
    doc.appendChild(root)
    return doc.toxml()

def getAll(request):
    course = Course()
    courseInfo = course.getCourse()
    doc = dm.Document()
    root = doc.createElement("课程列表")
    for item in courseInfo:
        c = doc.createElement("课程")
        cid = doc.createElement("课程编号")
        cid.appendChild(doc.createTextNode(item[0]))
        c.appendChild(cid)
        cnm = doc.createElement("课程名称")
        cnm.appendChild(doc.createTextNode(item[1]))
        c.appendChild(cnm)
        credit = doc.createElement("学分")
        credit.appendChild(doc.createTextNode(item[2]))
        c.appendChild(credit)
        tnm = doc.createElement("授课老师")
        tnm.appendChild(doc.createTextNode(item[3]))
        c.appendChild(tnm)
        croom = doc.createElement("授课地点")
        croom.appendChild(doc.createTextNode(item[4]))
        c.appendChild(croom)
        share = doc.createElement("共享")
        share.appendChild(doc.createTextNode(item[5]))
        c.appendChild(share)
        root.appendChild(c)
    doc.appendChild(root)
    return HttpResponse(doc.toxml(),"text/xml")