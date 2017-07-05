#_*_ coding:utf-8 _*_

import tushare as ts
import urllib.request
import datetime
import time

proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

todaydata = ts.get_stock_basics()

def loop_all_stocks():
    print('5>10>20')
    for eachid in todaydata.index:
        if is_break_high(eachid):
            print(eachid)
            #print(todaydata.index[eachid]['name'].decode('utf-8'))

def is_break_high(stockid):
    end_day = datetime.date.today()
    #start_day = end_day - datetime.timedelta(1)
    #start_day = start_day.strftime('%Y-%m-%d')
    end_day = end_day.strftime('%Y-%m-%d')
    df = ts.get_hist_data(stockid, start=end_day, end=end_day)

    ma5price = df['ma5'].max()
    ma10price = df['ma10'].max()
    ma20price = df['ma20'].max()

    if ma5price >= ma10price:
        if ma10price >= ma20price:
            return True
    else:
        return False

loop_all_stocks()