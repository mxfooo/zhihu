<<<<<<< HEAD
#_*_ coding:utf-8 _*_
import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
#https://ask.hellobi.com/blog/cuiqingcai/5540
#http://bbs.tianya.cn/list-funinfo-1.shtml

#ip代理上网
proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
#proxy = urllib.request.ProxyHandler({'https':'https://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

url = 'http://bbs.tianya.cn/list-funinfo-1.shtml'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

getdata = urllib.request.urlopen(url)
getinfo = getdata.read().decode('utf-8')
#pattern = re.compile("class=\"face\" title=\"([\u4e00-\u9fa5\w]+)\"")
#pattern = re.compile("td title=\".*\"")
#pattern = re.compile("class=\"author\">.*</a>")
#pattern = re.compile("target=\"_blank\">\s\"([\u4e00-\u9fa5\w]+)\"<span")
#items = re.findall(pattern, getinfo)
#print(items)

#print(getinfo)
#soup = BeautifulSoup(getinfo,'html.parser')
#print(soup.find_all('span'))

soup = BeautifulSoup(getinfo,'html5lib')
#print(soup)
#print(soup.find_all('span',{'class':'face'}))
#soupdata = soup.find_all('td',"td-title")

soupdata = soup.find_all('tr',"bg")
#print(soupdata)
for item in soupdata:
    title = item.find('span',"face").attrs['title']
    #content = item.find('td',"td-title").a.get_text()
    writetime = item.get_text().split()
    #author = item.find('a', "author").get_text()
    #strip()去掉空格符
    #split()根据空格进行分组
    print(
        "帖子：%s\n"
        "标题：%s\n"
        "作者: %s\n"
        "阅读量:%s\n"
        "回复量:%s\n"
        "发帖时间:%s"
    %(title,writetime[0],writetime[1],writetime[2],writetime[3],writetime[4]+":"+writetime[5]))
=======
#_*_ coding:utf-8 _*_
import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
#https://ask.hellobi.com/blog/cuiqingcai/5540
#http://bbs.tianya.cn/list-funinfo-1.shtml

#ip代理上网
proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
#proxy = urllib.request.ProxyHandler({'https':'https://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

url = 'http://bbs.tianya.cn/list-funinfo-1.shtml'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

getdata = urllib.request.urlopen(url)
getinfo = getdata.read().decode('utf-8')
#pattern = re.compile("class=\"face\" title=\"([\u4e00-\u9fa5\w]+)\"")
#pattern = re.compile("td title=\".*\"")
#pattern = re.compile("class=\"author\">.*</a>")
#pattern = re.compile("target=\"_blank\">\s\"([\u4e00-\u9fa5\w]+)\"<span")
#items = re.findall(pattern, getinfo)
#print(items)

#print(getinfo)
#soup = BeautifulSoup(getinfo,'html.parser')
#print(soup.find_all('span'))

soup = BeautifulSoup(getinfo,'html5lib')
#print(soup)
#print(soup.find_all('span',{'class':'face'}))
#soupdata = soup.find_all('td',"td-title")

soupdata = soup.find_all('tr',"bg")
#print(soupdata)
for item in soupdata:
    title = item.find('span',"face").attrs['title']
    #content = item.find('td',"td-title").a.get_text()
    writetime = item.get_text().split()
    #author = item.find('a', "author").get_text()
    #strip()去掉空格符
    #split()根据空格进行分组
    print(
        "帖子：%s\n"
        "标题：%s\n"
        "作者: %s\n"
        "阅读量:%s\n"
        "回复量:%s\n"
        "发帖时间:%s"
    %(title,writetime[0],writetime[1],writetime[2],writetime[3],writetime[4]+":"+writetime[5]))
>>>>>>> 331b4248e424fdea007c335637ec47d198717abe
