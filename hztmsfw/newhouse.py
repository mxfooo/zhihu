
from zhihu.hztmsfw.sqlhelper import sqlhelper

class newhouse(object):
    def __init__(self):
        self.__help=sqlhelper()
    
    def checkym(self,ym):
        sql = "select * from nhouse where ym= %s " % ym
        return self.__help.checkym(sql,)

    def addnhouse(self,ym,nhouse):
        sql="insert into nhouse(ym,nhouse) value(%s,%s)" % (ym,nhouse)
        return self.__help.addnhouse(sql,)

    def checkoym(self,ym):
        sql = "select * from ohouse where ym= %s " % ym
        return self.__help.checkym(sql,)

    def addohouse(self,ym,oldhouse):
        sql="insert into ohouse(ym,oldhouse) value(%s,%s)" % (ym,oldhouse)
        return self.__help.addnhouse(sql,)


        
        
        
    
    