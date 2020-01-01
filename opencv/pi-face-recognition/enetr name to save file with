import socket
from ssh2.session import Session


#simple program to log into ssh and use ls command
host = '192.168.43.127'
user ='pi'
password='amazing'

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,22))
session=Session()
session.handshake(sock)
session.userauth_password(user,password)
channel =session.open_session()
channel.execute("ls")
data =[]
data =list(channel.read())
print(data)
channel.close()
print("exit:{0}".format(channel.get_exit_status()))