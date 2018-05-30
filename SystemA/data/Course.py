from .Connect import Connection
import numpy as np

class Course:
    def getCourse(self,sid):
        conn=Connection()
        sql="SELECT * FROM dbo.课程;"
        result=conn.query(sql)
        print(result)
        for i in range(0,len(result)):
            result[i]=list(result[i])
            result[i].append(False)
        print(result)

        sql="SELECT * FROM dbo.选课 WHERE 学生编号='"+sid+"';"
        sresult=conn.query(sql)
        for i in range(0,len(sresult)):
            cid=int(sresult[i][0])
            result[cid][6]=True

        return result
        pass

    def selectCourse(self,sid,cid):
        conn=Connection()
        sql="INSERT INTO dbo.选课 VALUES ('"+cid+"','"+sid+"',NULL);"
        try:
            conn.update(sql)
        except Exception as e:
            conn.close()
            return False
        conn.close()
        return True


    def dropCourse(self,sid,cid):
        conn=Connection()
        sql="DELETE FROM dbo.选课 WHERE 课程编号='"+cid+"' AND 学生编号='"+sid+"';"
        try:
            conn.update(sql)
        except Exception as e:
            conn.close()
            return False
        conn.close()
        return True