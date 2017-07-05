
from module.userinfo import userinfo
from module.qa import qa
from tsokect.server import robot
import socketserver


def main():
    name=input('input your name:')
    pwd=input('input your password:')
    info=userinfo()
    result=info.check(name,pwd)
    
    if not result:
        print('login fail--name and password is mismatch')
    else:
        print('welcome %s.login success' %name)
        print('let us talk')
    
    server=socketserver.ThreadingTCPServer(('127.0.0.1',9999),robot)
    server.serve_forever()
    
    

if __name__=='__main__':
    main()
    
    