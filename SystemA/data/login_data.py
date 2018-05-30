from .Connect import Connection
import numpy as np

def login_data(account,password):
    connection=Connection()
    sql="SELECT * FROM dbo.账户 WHERE 账户名='"+account+"';"
    result=connection.query(sql)
    row=np.array(result)
    if row[1]!=password:
        return False
    else:
        return True
