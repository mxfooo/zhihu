#_*_coding:utf-8 _*_
import urllib
import urllib.request
from bs4 import BeautifulSoup
import http.cookiejar
import gzip
import re
import urllib.parse
import urllib.error

#https://zhuanlan.zhihu.com/p/23553649
#https://www.zhihu.com/question/29925879

#ip代理上网
#proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
proxy = urllib.request.ProxyHandler({'https':'https://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

url = 'https://www.zhihu.com/#signin'

getdata = urllib.request.urlopen(url)
getinfo = getdata.read().decode('utf-8')
soup = BeautifulSoup(getinfo,'html5lib')

