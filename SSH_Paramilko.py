import paramiko
import time
from getpass import getpass



#ip = '10.225.8.6'  - подключиться на один ip-адрес
#ip = ['10.3.159.170', '10.3.159.171']  - подключиться на несколько ip-адресов
username = 'netteam'
password = 'Qwerty123'


with open('test.txt') as hosts:
    for line in hosts:
        if line.startswith('10'):
            ip = line.split('\n')
            SESSION = paramiko.SSHClient()
            SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            SESSION.connect(hostname=ip[0], port=22, username=username, password=password, look_for_keys=False, allow_agent=False)
            DEVICE_ACCESS = SESSION.invoke_shell()
            #DEVICE_ACCESS.send(b'term length 0\n')  - command for cisco
            DEVICE_ACCESS.send(b'system-view\n')
            DEVICE_ACCESS.send(b'sysname Routers1\n')
            DEVICE_ACCESS.send(b'quit\n')
            time.sleep(2)
            output = DEVICE_ACCESS.recv(65000)
            print (output.decode('ascii'))
            SESSION.close
        else:
            ip2 = line.split('\n')
            print(ip2[0])

print('End Script')

