#_*_ coding:utf-8 _*_
import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
from urllib import parse
import datetime
import time
from zhihu.hztmsfw.newhouse import newhouse

#ip代理上网
proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
#proxy = urllib.request.ProxyHandler({'https':'https://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

#获取年份
def getyear():
    y = datetime.date.today()
    y = y.strftime('%Y')
    print(y)
    return

def lastyeat():
    y = datetime.date.today()
    y = int(y.strftime('%Y')) - 1
    print(y)
    return

url = 'http://www.tmsf.com/hzweb/newhouse/'
url2 = 'http://www.tmsf.com/hzweb/esf/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

getdata = urllib.request.urlopen(url)
getinfo = getdata.read().decode('utf-8')
getdata2 = urllib.request.urlopen(url2)
getinfo2 = getdata2.read().decode('utf-8')

def gethouse():
    pattern1 = re.compile("var ss2=\[(.*?)\]")
    items1 = pattern1.search(getinfo)
    #print(items1.group())
    nhouse = items1.group(1).split(",")
    #print(nhouse)
    return nhouse

def getmonth():
    pattern2 = re.compile("var ticks2=\[(.*?)\]")
    items2 = pattern2.search(getinfo)
    #print(items2.group())
    months = items2.group(1).split(",")
    #print(months)
    return months

def getoldhouse():
    pattern1 = re.compile("data : \[(.*?)\]")
    items1 = pattern1.search(getinfo2)
    #print(items1.group())
    oldhouse = items1.group(1).split(",")
    #print(oldhouse)
    return oldhouse

def getmonth2():
    pattern2 = re.compile("labels : \[(.*?)\]")
    items2 = pattern2.search(getinfo2)
    #print(items2.group())
    months = items2.group(1).split(",")
    #print(months)
    return months


def wnhouse():
    for v1,v2 in zip(getmonth(),gethouse()):
        result = nh.checkym(v1)
        if not result:
            nh.addnhouse(v1,v2)
        else:
            print("%s data is exist" %v1)
    print('Get data finished')
def wohouse():
    for v3,v4 in zip(getmonth2(),getoldhouse()):
        result2  = nh.checkoym(v3)
        if not result2:
            nh.addohouse(v3,v4)
        else:
            print("%s data is exist" % v3)
    print('Get oldhouse data finished.')

nh = newhouse()
wnhouse()
wohouse()








