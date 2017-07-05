#_*_ coding:utf-8 _*_

#输入时间找着星期几
import datetime

def get_birthday_weekday(birthday_str=None):
    weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if birthday_str == None:
        birthday = datetime.datetime.today()
        birthday_str =str(datetime.datetime.today())
    else:
        birthday =datetime.datetime.strptime(birthday_str,'%Y-%m-%d')
    print('Your birthday is %s is %s' %(birthday_str,weekdays[birthday.weekday()]))

gf_birthday = '2017-2-28'
bf_birthday = '1983-11-18'
print (type(gf_birthday))

get_birthday_weekday()
get_birthday_weekday(gf_birthday)
get_birthday_weekday(bf_birthday)