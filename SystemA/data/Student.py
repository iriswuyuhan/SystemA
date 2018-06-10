from .Connect import Connection
import xml.dom.minidom as dm

class Student:
    def getStu(self,account):
        conn=Connection()
        sql="SELECT * FROM dbo.学生 WHERE 关联账户='"+account+"';"
        result=conn.query(sql)
        conn.close()
        return result

    def getAll(self):
        conn=Connection()
        sql="SELECT * FROM dbo.学生;"
        result=conn.query(sql)
        conn.close()
        return result

    def getAccount(self,account):
        conn = Connection()
        sql = "SELECT * FROM dbo.账户 WHERE 账户名='" + account + "';"
        result = conn.query(sql)
        conn.close()
        return result

    def addStudent(self,xmlDom):
        conn=Connection()
        account=xmlDom.getElementsByTagName("账户名")[0].firstChild.data
        password=xmlDom.getElementsByTagName("密码")[0].firstChild.data
        auth=xmlDom.getElementsByTagName("权限")[0].firstChild.data

        sql="INSERT INTO dbo.账户 VALUES ('"+account+"','"+password+"','"+auth+"');"
        conn.update(sql)

        sid = xmlDom.getElementsByTagName("学号")[0].firstChild.data
        dep=xmlDom.getElementsByTagName("院系")[0].firstChild.data
        snm = xmlDom.getElementsByTagName("姓名")[0].firstChild.data
        sgen = xmlDom.getElementsByTagName("性别")[0].firstChild.data

        sql="INSERT INTO dbo.学生 VALUES ('"+sid+"','"+snm+"','"+sgen+"','"+dep+"','"+account+"');"
        conn.update(sql)

        conn.close()