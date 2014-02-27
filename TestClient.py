import socket 

host = 'localhost' 
port = 60000
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send('toggle,blue,2') 
print 'Sent'
