import pymysql
from zhihu.hztmsfw import conf

class sqlhelper(object):
    
    def __init__(self):
        self.conn_dict=conf.conn_dict
            
    def checkym(self,sql,):
        conn=pymysql.connect(**conf.conn_dict)
        cur=conn.cursor()
        
        rec=cur.execute(sql,)
        data=cur.fetchone()
        
        cur.close()
        conn.close()
        
        return data

    def addnhouse(self,sql,):
        conn=pymysql.connect(**conf.conn_dict)
        cur=conn.cursor()
        
        rec=cur.execute(sql,)
        conn.commit()
        
        cur.close()
        conn.close()



        
        
        
        
        
        
        
        