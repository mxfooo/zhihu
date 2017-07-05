#_*_ coding:utf-8 _*_

import tushare as ts
import urllib.request
import datetime
import time
#http://www.30daydo.com/article/70

proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)


todaydata = ts.get_stock_basics()
mydays = 120

def loop_all_stocks():
    print('shou pan zhan shang %s'%mydays)
    for eachid in todaydata.index:
        if is_break_high(eachid, mydays):
            print(eachid)
            #print(todaydata.index[eachid]['name'].decode('utf-8'))


def is_break_high(stockid,days):
    end_day = datetime.date.today()
    days = days*7/5
    start_day = end_day-datetime.timedelta(days)
    start_day = start_day.strftime('%Y-%m-%d')
    end_day = end_day.strftime('%Y-%m-%d')
    df = ts.get_hist_data(stockid, start=start_day, end=end_day)
    #time.sleep(10.0)
    period_high = df['high'].max()
    # print period_high
    today_high = df.iloc[0]['high']
    # 这里不能直接用 .values
    # 如果用的df【：1】 就需要用.values
    # print today_high
    if today_high >= period_high:
        return True
    else:
        return False

loop_all_stocks()