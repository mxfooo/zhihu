#_*_ coding:utf-8 _*_
import urllib
import urllib.request
from bs4 import BeautifulSoup

#ip代理上网
proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
#proxy = urllib.request.ProxyHandler({'https':'https://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

class spider:
    def __init__(self):
        self.siteurl = 'http://list.jd.com/list.html?cat=9987,653,655'

    def getpage(self,pageindex):
        url = self.siteurl+"?page="+str(pageindex)
        print(url)
        getdata = urllib.request.urlopen(url)
        getinfo = getdata.read().decode('utf-8')
        print(getinfo)
        return getinfo

    def getcontents(self,pageindex):
        page = self.getpage(pageindex)
        patten = re.compile('<strong>.*</strong>',re.S)
        items = re.findall(patten,page)
        print(items)


spider = spider()
spider.getcontents(1)