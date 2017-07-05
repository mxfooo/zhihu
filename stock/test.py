
import tushare as ts
import urllib.request

proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

#df = ts.inst_tops()
#df = ts.top_list('2017-05-08')
df = ts.cap_tops()
df.to_csv('d:/temp/cap.csv')
print(df)