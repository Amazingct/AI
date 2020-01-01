import socket, time
from ssh2.session import Session
import os
import sys

host = '192.168.43.29'
user ='pi'
password='amazing'

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,22))
session=Session()
session.handshake(sock)
session.userauth_password(user,password)
channel =session.open_session()
#cd into Desktop/sharedFiles
#copy content of shared file to my laptop
#channel.execute("scp frame.txt amazing@192.168.43.246:~/Desktop/SharedFiles/")
channel.shell()
channel.write("cd /home/pi\n")
channel.write("cd Desktop/sharedFiles\n")

channel.write("ls\n")
channel.write("scp now.txt pi@192.168.43.29:/home/pi/Desktop/sharedFiles\n")
stdin.put("amazing\n")
time.sleep(3)


#make a clean output
size, data =channel.read()
print(data.decode())
channel.close()

print("exit:{0}".format(channel.get_exit_status()))