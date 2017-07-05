#_*_ coding:utf-8 _*_
import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
import json
#https://zhuanlan.zhihu.com/p/25592334
#http://www.toutiao.com/search_content/?offset=80&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1

#ip代理上网
proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
#proxy = urllib.request.ProxyHandler({'https':'https://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

url = 'http://www.toutiao.com/search_content/?offset=80&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1'
url2 = 'http://www.toutiao.com/a6374530550295691778/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
'''
with urllib.request.urlopen(url) as getdata:
    getinfo = json.loads(getdata.read().decode())
print(getinfo)
'''
getdata = urllib.request.urlopen(url2)
getinfo = getdata.read().decode('utf-8')
soup = BeautifulSoup(getinfo,'html5lib')

#article_content = soup.find_all('div',"article-content")
#item.find('img').get('src')
#for item in article_content:
#    print(item.find('img').get('src'))
article_content = soup.find('h1',"article-title").get_text()
print(article_content)

'''
for link in soup.find_all('img',img_height=True):
    photo_list = link.get('src')
    photo_name = photo_list.rsplit('/',1)[-1]+'.jpg'

    with urllib.request.urlopen(photo_list) as res, open(photo_name,'wb') as f:
        f.write(res.read())
'''