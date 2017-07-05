#_*_ coding:utf-8 _*_
import time
import paramiko
import sys
import os
import re
class Sign():
    
    SSHHost     = '10.106.209.14'
    SSHPort     = 22
    SSHUsr      = 'toor4nsn'
    SSHPsw      = 'oZPS0POrRieRtu'
    SSHTimeout  = 10

    def login(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(Sign.SSHHost, Sign.SSHPort,username=Sign.SSHUsr,password=Sign.SSHPsw,timeout=Sign.SSHTimeout)


        time.sleep(2)
        print('login success')
        stdin, stdout, stderr = client.exec_command('pwd')
        print(stdout.read())
        stdin, stdout, stderr = client.exec_command('uboot_env get')
        #print(stdout.read())
        s = str(stdout.read())
        print(s)
        pattern1 = re.compile("active_partition=(\d)")
        items1 = pattern1.search(s)
        print(items1.group())
        client.close()
        print('logout success')

if __name__ == '__main__':
    sign = Sign()
    sign.login()
            


            
