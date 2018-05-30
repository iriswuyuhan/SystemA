from .Connect import Connection


class Student:
    def getSid(self,account):
        conn=Connection()
        sql="SELECT * FROM dbo.学生 WHERE 关联账户='"+account+"';"
        result=conn.query(sql)
        conn.close()
        return result[0][0]
