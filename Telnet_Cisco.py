
from telnetlib import Telnet


#cmd = input('Enter the command: ')

tn = Telnet('10.225.8.6')
tn.write(b'netteam\n')
tn.write(b'Ytyfdb;eRblfk202@\n')
tn.write(b'term length 0\n')
#tn.write(cmd.encode('ascii') + b'\n')
tn.write(b'conf t\n')
tn.write(b'vlan 349\n')
tn.write(b'exit\n')
tn.write(b'exit\n')
tn.write(b'exit\n')

print (tn.read_all().decode('ascii'))