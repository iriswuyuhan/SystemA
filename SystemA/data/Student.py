from .Connect import Connection

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
