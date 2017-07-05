#_*_ coding:utf-8 _*_
import urllib
import re
import urllib.request
from bs4 import BeautifulSoup

#ip代理上网
proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
#proxy = urllib.request.ProxyHandler({'https':'https://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

#https://zhuanlan.zhihu.com/p/25592334
#http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1
url = 'http://list.jd.com/list.html?cat=9987,653,655'

class tieba():
    def __init__(self,baseurl):   #  这里应该是__init__
        self.baseurl = baseurl

    def getpage(self,pagenum):
        try:
            url = self.baseurl
            getdata = urllib.request.urlopen(url)
            getinfo = getdata.read().decode('utf-8')
            print(getinfo)
            return getdata
        except urllib.request.URLError as e:
            if hasattr(e,"reson"):
                print("error reason:%s" %e.reason)
                return None

baseurl = 'http://list.jd.com/list.html?cat=9987,653,655'
gtieba = tieba(baseurl)
gtieba.getpage(1)





