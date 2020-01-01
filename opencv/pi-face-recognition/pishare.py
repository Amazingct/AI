import socket
s = socket.socket()
host = input(str("pls enter host a ddr: "))
port = 8081
s.connect((host,port))
print("connected")

filename = input(str("enetr name to save file with"))
file=open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("file has been received")
