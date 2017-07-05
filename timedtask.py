#_*_ coding:utf-8 _*_
import platform
import os
import datetime

def runtask():
    os_platform = platform.platform()
    if os_platform.startswith('Darwin'):
        print('This is mac os system')
        os.system('ls')
    elif os_platform.startswith('Window'):
        print('This is win system')
        os.system('dir')

def timerfun(sched_Timer):
    flag = 0
    while True:
        now = datetime.datetime.now()

        if now >= sched_Timer:
            runtask()
            flag = 1
        else:
            if flag == 1:
                sched_Timer = sched_Timer+datetime.timedelta(minutes=1)
                flag = 0

if __name__ == '__main__':
    sched_Timer = datetime.datetime(2017,2,28,16,47,30)
    print('run the timer task at %s'%sched_Timer)
    timerfun(sched_Timer)





