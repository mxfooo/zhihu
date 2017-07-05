#_*_ coding:utf-8 _*_
import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
import json
import os
from urllib import parse
import traceback
import sys
#https://zhuanlan.zhihu.com/p/25592334
#http://www.toutiao.com/search_content/?offset=80&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1
#代码参考：https://github.com/zmrenwu/toutiao/blob/master/jiepai.py


def create_dir(name):
    if not os.path.exists(name):
        os.mkdir(name)
    return

#def get_url():

#ip代理上网
proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
#proxy = urllib.request.ProxyHandler({'https':'https://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

url = 'http://www.toutiao.com/search_content/?offset=80&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1'
url2 = 'http://www.toutiao.com/a6374530550295691778/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

offset = 20
query_data = {
            'offset': offset,
            'format': 'json',
            'keyword': '街拍',
            'autoload': 'true',
            'count': 20,  # 每次返回 20 篇文章
            'cur_tab': 1
        }
#通过parse.urlencode函数把字典转化成字符串
get_url = parse.urlencode(query_data)
query_url = 'http://www.toutiao.com/search_content/' + '?'+get_url

def get_artcile_urls(req):
    getdata = urllib.request.urlopen(req)
    d = json.loads(getdata.read().decode()).get('data')
    if d is None:
        print("dayin wancheng")
        return

    urls = [article.get('article_url') for article in d if article.get('article_url')]
    return urls

if __name__ == '__main__':
    artcile_urls = get_artcile_urls(query_url)
    for item in artcile_urls:

        getdata = urllib.request.urlopen(item)
        getinfo = getdata.read().decode('utf-8')
        soup = BeautifulSoup(getinfo,'html5lib')
        print(item)

        dir = './jiepai'
        create_dir(dir)
        #判断，如果是视频，直接跳过

        try:
            file_name = soup.find('h1', "article-title").get_text()
            print(file_name)
            if  file_name != None:
                create_dir(dir+"/"+file_name)

                for link in soup.find_all('img',img_height=True):
                    photo_list = link.get('src')
                    photo_name = photo_list.rsplit('/',1)[-1]+'.jpg'
                    save_path = os.path.join(dir,file_name,photo_name)

                    with urllib.request.urlopen(photo_list) as res, open(save_path,'wb') as f:
                        f.write(res.read())
        except KeyboardInterrupt:
            print("你已经使用ctrl+F2结束程序了")
            sys.exit()
        except Exception:
            exinfo = traceback.format_exc()
            print(exinfo)
