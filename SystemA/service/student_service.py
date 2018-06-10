from django.http import HttpResponse
from ..data.Student import Student
import xml.dom.minidom as dm

def addStu(request):
    student=Student()
    bodydata=request.body
    doc=dm.parseString(bodydata)
    student.addStudent(doc)
    return HttpResponse(True)

def getAll(request):
    student=Student()
    stuInfo=student.getAll()
    result=wrapStu(stuInfo)
    return HttpResponse(result,"text/xml")
    pass

def getStu(request):
    student=Student()
    stuInfo=student.getStu(request.GET.get('account'))
    result=wrapStu(stuInfo)
    return HttpResponse(result,"text/xml")

def wrapStu(stuInfo):
    student=Student()
    doc=dm.Document()
    root=doc.createElement("学生列表")
    for item in stuInfo:
        stu=doc.createElement("学生信息")
        sid=doc.createElement("学号")
        sid.appendChild(doc.createTextNode(item[0]))
        stu.appendChild(sid)
        snm=doc.createElement("姓名")
        snm.appendChild(doc.createTextNode(item[1]))
        stu.appendChild(snm)
        sgen=doc.createElement("性别")
        sgen.appendChild(doc.createTextNode(item[2]))
        stu.appendChild(sgen)
        sdep=doc.createElement("院系")
        sdep.appendChild(doc.createTextNode(item[3]))
        stu.appendChild(sdep)
        sacc=doc.createElement("账户名")
        sacc.appendChild(doc.createTextNode(item[4]))
        stu.appendChild(sacc)
        account=item[4]
        aresult=student.getAccount(account)
        spwd=doc.createElement("密码")
        spwd.appendChild(doc.createTextNode(aresult[0][1]))
        stu.appendChild(spwd)
        sauth=doc.createElement("权限")
        sauth.appendChild(doc.createTextNode(aresult[0][2]))
        stu.appendChild(sauth)
        root.appendChild(stu)
    doc.appendChild(root)
    return doc.toxml()